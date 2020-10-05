var gulp = require("gulp");
var cssnano = require("gulp-cssnano");
var rename = require("gulp-rename");
var uglify = require('gulp-uglify');
var concat = require('gulp-concat');
var imagemin = require('gulp-imagemin');
var cache = require('gulp-cache');
var bs = require('browser-sync').create();
var sass = require('gulp-sass');
// js报错不会直接退出
var util = require('gulp-util');
// 清楚打印js报错信息
var sourcemaps = require('gulp-sourcemaps');

// 定义统一路径
var path = {
    'html': './templatetags/**/',
    'css': './src/css/**/',
    'js': './src/js/',
    'images': './src/images/',
    'css_dist': './dist/css/',
    'js_dist': './dist/js/',
    'images_dist': './dist/images/'
};

// 处理html文件的任务
gulp.task('html', function (done) {
    gulp.src(path.html + '*.html')
        .pipe(bs.stream())
    done();
});

// 定义一个css的任务
gulp.task('css', function (done) {
    gulp.src(path.css + '*.scss')
        .pipe(sass()).on('error', sass.logError)
        .pipe(cssnano())
        .pipe(rename({'suffix': '.min'}))
        .pipe(gulp.dest(path.css_dist))
        .pipe(bs.stream());
    done();
});

// 定义一个js的任务
gulp.task('js', function (done) {
    gulp.src(path.js + '*.js')
        .pipe(sourcemaps.init())
        .pipe(uglify()).on('error', util.log)
        .pipe(rename({'suffix': '.min'}))
        .pipe(gulp.dest(path.js_dist))
        .pipe(sourcemaps.write())
        .pipe(bs.stream());
    done();
});

// 定义一个处理图片文件的任务
gulp.task('images', function (done) {
    gulp.src(path.images + '*.*')
        .pipe(cache(imagemin()))
        .pipe(rename({'suffix': '.min'}))
        .pipe(gulp.dest(path.images_dist))
        .pipe(bs.stream());
    done();
});

// 定义监听文件修改的任务
gulp.task('watch', function (done) {
    gulp.watch(path.html + '*.html', gulp.series('html'));
    gulp.watch(path.css + '*.scss', gulp.series('css'));
    gulp.watch(path.js + '*.js', gulp.series('js'));
    gulp.watch(path.images + '*.*', gulp.series('images'));
    done();
});

// 初始化browser-sync的任务
gulp.task('bs', function (done) {
    bs.init({
        'server': {
            'bassDir': './'
        }
    });
    done();
});

// 创建一个默认的任务
// gulp.task('default', gulp.series('bs', 'watch'));
gulp.task('default', gulp.series('watch'));