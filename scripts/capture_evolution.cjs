/** Recreate historical home captures. Requires playwright and sharp (NODE_PATH supported).
 * node scripts/capture_evolution.cjs — exports committed sources into a temporary directory.
 * Originals remain in the printed temporary directory; only WebP assets enter the site.
 */
const {execFileSync, spawn} = require('node:child_process');
const fs = require('node:fs');
const path = require('node:path');
const os = require('node:os');
const {chromium} = require('playwright');
const sharp = require('sharp');
const root = path.resolve(__dirname, '..');
const {values: options} = require('node:util').parseArgs({options:{
 'desktop-only':{type:'boolean',default:false},
 commits:{type:'string'}
}});
const manifestPath = path.join(root, 'projects/portfolio-evolution/timeline.json');
const previous = options.commits ? JSON.parse(fs.readFileSync(manifestPath, 'utf8')) : null;
const selected = options.commits?.split(',');
const output = path.join(root, 'public/images/cases/portfolio-evolution');
const temp = fs.mkdtempSync(path.join(os.tmpdir(), 'portfolio-evolution-'));
const git = (...args) => execFileSync('git', args, {cwd:root, maxBuffer:100*1024*1024});
const notes = {
 c623256:['O ponto de partida','Referências visuais e conteúdo dos cases. O arquivo da home ainda estava vazio.'],
 '338d3e6':['A primeira home','Primeira implementação responsiva, com apresentação e quatro projetos.'],
 df69626:['Um caminho para conversar','Entrada do contato pelo WhatsApp na home e nos cases.'],
 a8049fd:['Registro de revisão','Capturas de revisão adicionadas ao repositório; sem alteração na home.'],
 c7f7233:['Conteúdo em Markdown','Migração dos textos dos cases para Markdown; sem alteração na home.'],
 f147112:['Revisão dos cases','Atualização das páginas dos projetos; sem alteração na home.'],
 '7e4a81d':['Imagens atualizadas','Atualização dos arquivos de imagem do Cervello usados no portfólio.'],
 db2f11a:['Uma apresentação mais elaborada','Nova composição da abertura, ícones e ajustes de hierarquia e imagens.'],
 '965b240':['Cor, tipografia e dois idiomas','Fundo amarelo, nova tipografia e navegação entre português e inglês.'],
 '8c59af2':['Ajustes de contraste e ritmo','Refinamento da cor do texto, das bordas e do espaçamento entre letras.'],
 '585f05b':['Imagens que levam aos cases','Composições dos projetos passam a funcionar como links; ajustes nos títulos dos cases.'],
 'cfa01e6':['Entender quem usa o produto','Nova abertura e revisão dos cases com foco na rotina de trabalho de quem usa os produtos. Hero passa a apresentar apenas texto.'],
 'd5d556e':['Navegação sempre à mão','Cabeçalho sticky, proporções revistas, contato simplificado e nova distribuição das imagens nos cases.']
};
(async()=>{
 fs.mkdirSync(output,{recursive:true});
 const commits=git('log','--reverse','--format=%H|%aI|%s','c623256ca7cfdb8051e493cb3468a84eb90058d4^..HEAD').toString().trim().split('\n');
 const server=require('node:http').createServer((req,res)=>{
 let file=path.join(temp,decodeURIComponent(new URL(req.url,'http://localhost').pathname));
 if(file.endsWith('/'))file+='index.html';
 const types={'.html':'text/html','.css':'text/css','.js':'text/javascript','.svg':'image/svg+xml','.png':'image/png','.webp':'image/webp'};
 fs.readFile(file,(err,data)=>{res.writeHead(err?404:200,{'Content-Type':types[path.extname(file)]||'application/octet-stream'});res.end(err?'Not found':data);});
 });
 await new Promise(resolve=>server.listen(8765,'127.0.0.1',resolve));
 let browser;
 try {
 for(let i=0;i<50;i++){try{await fetch('http://127.0.0.1:8765/');break;}catch{await new Promise(r=>setTimeout(r,100));}}
 browser=await chromium.launch({headless:true, executablePath:process.env.CHROME_PATH || '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'});
 const manifest={start:commits[0].split('|')[0],end:commits.at(-1).split('|')[0],capturedOn:new Date().toISOString(),browser:await browser.version(),locale:'pt-BR',timezone:'America/Sao_Paulo',viewports:{desktop:{width:1440,height:1000},mobile:{width:390,height:844}},commits:[]};
 const captureCommits = selected ? selected.map(ref => {
 const sha = git('rev-parse', '--verify', ref + '^{commit}').toString().trim();
 const line = commits.find(item => item.startsWith(sha + '|'));
 if (!line) throw new Error('Commit outside portfolio history: ' + ref);
 return line;
}) : commits;
 if (previous) manifest.commits = [...previous.commits];
 for(const line of captureCommits){
 const [sha,date,message]=line.split('|'); const short=sha.slice(0,7);
 const entry={sha,date,message,title:notes[short]?.[0]||message,description:notes[short]?.[1]||message,images:{}};
 if(!git('show',`${sha}:index.html`).length){entry.kind='reference'; manifest.commits.push(entry);continue;}
 entry.kind='capture';
 const dir=path.join(temp,short); fs.mkdirSync(dir);
 const available=git('ls-tree','--name-only',sha).toString().trim().split('\n');
 const paths=['index.html','css','js','projects','assets','public'].filter(p=>available.includes(p));
 const tar=path.join(temp,short+'.tar'); fs.writeFileSync(tar,git('archive',sha,...paths));
 execFileSync('tar',['-xf',tar,'-C',dir]);fs.unlinkSync(tar);
 for(const [device,viewport] of Object.entries(manifest.viewports)){
 if(options['desktop-only'] && device !== 'desktop') continue;
 const context=await browser.newContext({viewport,deviceScaleFactor:1,locale:'pt-BR',timezoneId:'America/Sao_Paulo',reducedMotion:'reduce',colorScheme:'light'});
 const page=await context.newPage(); const failed=[];
 page.on('requestfailed',r=>failed.push(r.url()));
 await page.goto(`http://127.0.0.1:8765/${short}/`,{waitUntil:'networkidle'});
 await page.addStyleTag({content:'*,*::before,*::after{animation:none!important;transition:none!important;caret-color:transparent!important}'});
 await page.evaluate(async()=>{document.querySelectorAll('img').forEach(i=>i.loading='eager'); await document.fonts.ready; await Promise.all([...document.images].map(i=>i.decode().catch(()=>{})));});
 const broken=await page.evaluate(()=>[...document.images].filter(i=>!i.naturalWidth).map(i=>i.src));
 if(broken.length||failed.length)throw new Error(JSON.stringify({short,device,broken,failed}));
 const base=`${date.slice(0,10)}-${short}-home-pt-${device}`;
 for(const [suffix,fullPage] of [['',true],['-viewport',false]]){
 const png=path.join(temp,base+suffix+'.png'); await page.screenshot({path:png,fullPage,animations:'disabled'});
 const name=base+suffix+'.webp';await sharp(png).webp({quality:84}).toFile(path.join(output,name));
 entry.images[device+(suffix?'Viewport':'')]=name;
 }
 await context.close();
 }
 const existing = manifest.commits.findIndex(item => item.sha === sha);
 if(existing >= 0) {
 entry.images = {...manifest.commits[existing].images, ...entry.images};
 manifest.commits[existing] = entry;
 } else manifest.commits.push(entry);
 console.log('Captured',short);
 }
 manifest.commits.sort((a,b) => commits.findIndex(line=>line.startsWith(a.sha+'|')) - commits.findIndex(line=>line.startsWith(b.sha+'|')));
 fs.writeFileSync(manifestPath,JSON.stringify(manifest,null,2)+'\n');
 console.log('Original PNGs:',temp);
 }finally{if(browser)await browser.close();server.close();}
})().catch(e=>{console.error(e);process.exitCode=1});
