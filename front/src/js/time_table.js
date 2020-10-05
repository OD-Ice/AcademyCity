function TimeTable () {

}

TimeTable.prototype.tableInit = function () {
    var courseTable = $('#coursesTable');
    var courseList = jQuery.parseJSON(courseTable.attr('data-weeks'));
    var week = window.innerWidth > 360 ? ['周一', '周二', '周三', '周四', '周五'] :
        ['一', '二', '三', '四', '五'];
    var day = new Date().getDay();
    var courseType = jQuery.parseJSON(courseTable.attr('data-course-type'));
    // 实例化(初始化课表)
    new Timetables({
        el: '#coursesTable',
        timetables: courseList,
        week: week,
        timetableType: courseType,
        highlightWeek: day,
        merge: false,
        gridOnClick: function (e) {
            var submitBtn = $('.submit-btn');
            submitBtn.attr('data-week', e.week);
            submitBtn.attr('data-course-time', e.index);
            acajax.post({
                'url': '/course/select_course/',
                'data': {
                    'week': e.week,
                    'index': e.index,
                },
                'success': function (result) {
                    var courses = result['data'];
                    var tpl = template("course-item", {'school_courses': courses, 'course_name': e.name});
                    var selectInput = $('#course-input');
                    selectInput.empty();
                    selectInput.append(tpl);
                }
            });
            // alert(e.name + '  ' + e.week + ', 第' + e.index + '节课, 课长' + e.length * 2 + '节');
            // console.log(e);
        },
        styles: {
            Gheight: 120
        }
    });
    var li = $('.Courses-content li');
    li.attr('data-toggle', 'modal');
    li.attr('data-target', '#course-modal');
}

TimeTable.prototype.submitCourseTableEvent = function () {
    var submitBtn = $('.submit-btn');
    var courseInput = $('#course-input');
    submitBtn.click(function () {
        var courseId = courseInput.val();
        var week = submitBtn.attr('data-week');
        var courseTime = submitBtn.attr('data-course-time');
        acajax.post({
            'url': '/course/submit_event/',
            'data': {
                'course_id': courseId,
                'week': week,
                'course_time': courseTime,
            },
            'success': function (result) {
                window.location.reload();
            }
        });
    });
};

TimeTable.prototype.run = function () {
    this.tableInit();
    this.submitCourseTableEvent();
};

$(function () {
    var time_table = new TimeTable();
    time_table.run();
});