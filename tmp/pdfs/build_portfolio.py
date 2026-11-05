from pathlib import Path
from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor, Color
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.utils import ImageReader
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle
R=Path('/Users/leandro/repos/portfolio')
pdfmetrics.registerFont(TTFont('Orelega',str(R/'tmp/pdfs/OrelegaOne-Regular.ttf')))
pdfmetrics.registerFont(TTFont('ArialNarrow','/System/Library/Fonts/Supplemental/Arial Narrow.ttf'))
W,H=960,600
BG=HexColor('#eef25e'); INK=HexColor('#35403f'); MUTED=HexColor('#53617a')
C=canvas.Canvas(str(R/'output/pdf/portfolio-leandro-oliveira.pdf'),pagesize=(W,H),pageCompression=1)
C.setTitle('Leandro Oliveira | Portfólio de Product Design'); C.setAuthor('Leandro Oliveira')
URL='https://oliveiraleandro.github.io/portfolio/'
def txt(t,x,y,size=12,font='ArialNarrow',color=INK):
 C.setFillColor(color); C.setFont(font,size); C.drawString(x,y,t)
def para(t,x,top,width,size=16,font='ArialNarrow',leading=21):
 p=Paragraph(t,ParagraphStyle('p',fontName=font,fontSize=size,leading=leading,textColor=INK)); _,h=p.wrap(width,200); p.drawOn(C,x,top-h)
def base(n):
 C.setFillColor(BG); C.rect(0,0,W,H,fill=1,stroke=0)
 txt('Leandro Oliveira',40,565,14); txt('Product Designer',40,548,11)
 txt('PORTFÓLIO',832,563,11)
 C.setStrokeColor(Color(.2,.25,.25,.18)); C.setLineWidth(.6); C.line(40,42,920,42)
 txt('oliveiraleandro.github.io/portfolio',40,25,10)
 C.linkURL(URL,(40,20,230,37),relative=0)
 txt(f'{n:02d} / 05',880,25,10)
def heading(num,title,desc,slug):
 base(num+1); txt(f'{num:02d}',40,492,14,color=MUTED); txt(title,75,486,32,'Orelega')
 para(desc,40,469,850,16,leading=20)
 C.bookmarkPage(slug); C.addOutlineEntry(title,slug,0)
 C.linkURL(URL+'projects/'+slug+'/',(75,482,650,522),relative=0)
def pic(path,x,y,w,h):
 im=Image.open(R/path).convert('RGBA')
 iw,ih=im.size; scale=min(w/iw,h/ih); dw,dh=iw*scale,ih*scale
 px=x+(w-dw)/2; py=y+(h-dh)/2
 C.setFillColor(Color(1,1,1,.24)); C.roundRect(px-5,py-5,dw+10,dh+10,4,fill=1,stroke=0)
 C.setFillAlpha(1)
 C.drawImage(ImageReader(im),px,py,dw,dh,mask='auto')
def img(project,name,*box): pic(f'projects/{project}/images/{name}',*box)
base(1)
txt('Design para quem',40,432,57,'Orelega'); txt('usa o produto.',40,369,57,'Orelega')
para('Investigo como as pessoas trabalham e desenho ferramentas<br/>que trazem mais clareza e autonomia ao dia a dia.',42,323,770,21,leading=27)
txt('Leandro Oliveira',42,196,27,'Orelega'); txt('Product Designer',42,169,18)
txt('SEBRAE  /  Sinapse Finance  /  Cervello BPMS  /  Iconatus · CAP',42,87,15)
C.showPage()
heading(1,'Ecossistema de Inovação SEBRAE','Desenhei uma plataforma que reúne avaliações de consultores e resultados para gestores, com a metodologia disponível durante o trabalho.','sebrae')
img('sebrae','Frame 2116.png',40,83,530,330)
img('sebrae','Frame 2117.png',595,252,325,180)
img('sebrae','Frame 2118.png',595,62,325,180)
C.showPage()
heading(2,'Sinapse Finance','Investiguei dificuldades nos formulários e redesenhei o fluxo. Para as automações financeiras, criei etapas visuais e configurações mais claras.','sinapse')
img('sinapse','automation-flow-white.png',40,66,380,365)
img('sinapse','image 6.png',444,91,204,310)
img('sinapse','image 8.png',670,91,250,310)
C.showPage()
heading(3,'Cervello BPMS','Redesenhei a rotina de suporte e implementei componentes reutilizáveis em HTML e SCSS, com personalização para diferentes marcas.','cervello')
img('cervello','cervello.png',40,219,545,211)
img('cervello','modo-claro.png',120,61,151,151)
img('cervello','modo-escuro.png',310,61,151,151)
for i,name in enumerate(['Group-2.png','Group.png','Group-1.png']): img('cervello',name,613+i*105,116,97,300)
C.showPage()
heading(4,'Iconatus · CAP','Adaptei a plataforma imobiliária ao desktop e ao celular, reorganizando informações de imóveis, atividades e comparações de preço.','iconatus')
img('iconatus','imoveis - precificacao v2.png',40,66,365,365)
img('iconatus','home v2.png',425,66,365,365)
img('iconatus','mobile resultado.png',813,66,107,365)
C.showPage()
C.save()
print(R/'output/pdf/portfolio-leandro-oliveira.pdf')
