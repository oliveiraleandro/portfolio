//node-modules
const gulp = require('gulp');
const {watch} = require('gulp');
const panini = require('panini');
const sass = require('gulp-sass')(require('sass'));
const del = require('del');
const csso = require('gulp-csso')
const autoprefixer = require('gulp-autoprefixer')
const purify = require('gulp-purifycss')
const ext_replace = require('gulp-ext-replace');


//Pasta para onde vão os arquivos compilados
const dist = './public/'

//Fontes
const srcFONTS = 'src/webfonts/**/*'
const srcIMG = 'src/img/**/*'
const srcJS = 'src/js/**/*.js'
const srcCSS = 'src/scss/**/*.scss'
const srcHTML = 'src/pages/**/*.**'
const srcFAV = 'src/favicon/*'
const srcROBOTS = 'src/robots/*'
const srcMAP = 'src/sitemap/*'

//Saída
const distFONTS = dist + 'webfonts/'
const distIMG = dist + 'img/'
const distJS = dist + 'js/'
const distCSS = dist
const distHTML = dist
const distFAV = dist
const distROBOTS = dist
const distMAP = dist


function moveFONTS(done) {
  return gulp.src(srcFONTS)
    .pipe(gulp.dest(distFONTS))
  done();
}


function moveIMG(done) {
  return gulp.src(srcIMG)
    .pipe(gulp.dest(distIMG))
  done();
}

function moveFAV(done) {
  return gulp.src(srcFAV)
    .pipe(gulp.dest(distFAV))
  done();
}

function moveJS(done) {
  return gulp.src(srcJS)
    .pipe(gulp.dest(distJS))
  done();
}

function moveROBOTS(done) {
  return gulp.src(srcROBOTS)
    .pipe(gulp.dest(distROBOTS))
  done();
}

function moveMAP(done) {
  return gulp.src(srcMAP)
    .pipe(gulp.dest(distMAP))
  done();
}

/* function moveHTML(done) {
  return gulp.src(srcHTML)
    .pipe(gulp.dest(distHTML))
  done();
} */



function templateHTML() {
  panini.refresh();
  return gulp.src(srcHTML)
    .pipe(panini({
      root: 'src/pages/',
      layouts: 'src/layouts/',
      partials: 'src/partials/',
      helpers: 'src/helpers/',
      data: 'src/data/'
    }))
    .pipe(ext_replace('.html'))
    .pipe(gulp.dest(distHTML))
}


function processaCSS(done) {
  return gulp.src(srcCSS)
    .pipe(sass({
      includePaths: ['node_modules/bootstrap/scss/']
    }))
    .pipe(sass().on('error', sass.logError))
    .pipe(gulp.dest('src/scss/'));
}

function clean(done) {
  done();
  return del(dist + '**/*', {
    force: true
  })
}

function otimizaCSS() {
  return gulp.src('src/scss/styles.css')
    .pipe(autoprefixer())
    //.pipe(purify([srcJS, 'src/pages/**/*.*','src/partials/**/*.*','src/layouts/**/*.*']))
    .pipe(csso())
    .pipe(gulp.dest(distCSS))
}



function watcher() {
  watch(srcFONTS, moveFONTS)
  watch(srcIMG, moveIMG)
  watch(srcJS, moveJS)
  watch(srcROBOTS, moveROBOTS)
  watch(srcMAP, moveMAP)
  watch(['src/{pages,layouts,partials,helpers,data}/**/*'], templateHTML)
  watch(srcCSS, gulp.series(processaCSS, otimizaCSS))

}


gulp.task('default', gulp.series(clean, gulp.parallel(moveFONTS, moveJS, moveROBOTS, moveMAP, moveFAV, templateHTML), processaCSS, otimizaCSS, moveIMG, watcher))

gulp.task('build', gulp.series(clean, gulp.parallel(moveFONTS, moveJS, moveROBOTS, moveMAP, moveFAV, templateHTML), processaCSS, moveIMG, otimizaCSS))