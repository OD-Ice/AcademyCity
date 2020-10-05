function PublishCourse() {
    selectorx = $('.duallistbox').bootstrapDualListbox({
    nonSelectedListLabel: '未选课程',
    selectedListLabel: '本校课程',
    filterTextClear: '<span class="badge badge-primary">清除筛选</span>',
    infoTextFiltered: '<span class="badge badge-warning">筛选</span> {0} from {1}',
    infoText: '已选/未选 {0}' ,
    infoTextEmpty: '空',
    filterPlaceHolder: '筛选条件',
    });
}

PublishCourse.prototype.listenDefineEvent = function () {
    var defineBtn = $('.define-btn');
    defineBtn.click(function () {
        var values = selectorx.val();
        var school_id = $(this).attr('data-school-id');
        acajax.post({
            'url': '/course/select_school_course/',
            'traditional':true,
            'dataType': 'json',
            'data': {
                'course_ids': JSON.stringify(values),
                'school_id': school_id,
            },
            'success': function (result) {
                acalert.alertSuccess({
                    'msg': '修改成功！',
                    'confirmCallback': function () {
                        window.location.reload();
                    }
                })
            }
        });
    });
};

PublishCourse.prototype.listenAddCourseEvent = function () {
    var submitBtn = $('.submit-btn');
    var courseInput = $('#course-input');
    var weekdayInput = $('#weekday-input');
    var timeInput = $('#time-input');
    submitBtn.click(function () {
        var course_name = courseInput.val();
        var week_day_id = weekdayInput.val();
        var course_time_id = timeInput.val();
        acajax.post({
            'url': '/course/add_course/',
            'data': {
                'course_name': course_name,
                'week_day_id': week_day_id,
                'course_time_id': course_time_id,
            },
            'success': function (result) {
                $('#course-modal').modal('hide');
                var course_id = result['data']['id'];
                var week_day = result['data']['week_day'];
                var course_time = result['data']['course_time'];
                selectorx.append('<option value='+course_id+'>'+course_name+'&nbsp;&nbsp;&nbsp;&nbsp;//&nbsp;&nbsp;&nbsp;&nbsp;'+week_day+'&nbsp;&nbsp;&nbsp;&nbsp;//&nbsp;&nbsp;&nbsp;&nbsp;'+course_time+'</option>');
                selectorx.bootstrapDualListbox('refresh');
            }
        })
    });
};

PublishCourse.prototype.run = function () {
    this.listenDefineEvent();
    this.listenAddCourseEvent();
};

$(function () {
    var pubCourse = new PublishCourse();
    pubCourse.run();
});