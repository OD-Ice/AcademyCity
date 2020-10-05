function StudentList() {

}

StudentList.prototype.listenEditEvent = function () {
    var submitBtn = $('.submit-btn');
    var levelInput = $('#level-input');
    submitBtn.click(function (event) {
        event.preventDefault();
        var studentId = submitBtn.data('student-id');
        var level = levelInput.val();
        acajax.post({
            'url': '/student/student_list/',
            'data': {
                'student_id': studentId,
                'level_id': level,
            },
            'success': function (result) {
                window.location.reload();
            }
        });
    });
};

StudentList.prototype.listenDelEvent = function () {
    var delBtn = $('.del-btn');
    delBtn.click(function (event) {
        event.preventDefault();
        var student_id = $(this).attr('data-student-id');
        var student_name = $(this).attr('data-student-name');
        acalert.alertConfirm({
            'msg': '确定要开除'+student_name+'吗?',
            'confirmCallback': function () {
                acajax.post({
                    'url': '/student/del_student_school/',
                    'data': {
                        'student_id': student_id
                    },
                    'success': function (result) {
                        acalert.alertSuccess({
                            'title': '欧耶~',
                            'msg': '恭喜你毁了'+student_name+'的未来！TA辍学了！',
                            'confirmCallback': function () {
                                window.location.reload();
                            }
                        });
                    }
                })
            }
        });
    });
};

StudentList.prototype.run = function () {
    this.listenDelEvent();
    this.listenEditEvent();
};

$(function () {
    var student_list = new StudentList();
    student_list.run();

    $('#level-modal').on('show.bs.modal', function (event) {
        var button = $(event.relatedTarget);
        var submitBtn = $('.submit-btn');
        var studentSuperpower = button.data('student-superpower');
        var studentId = button.data('student-id');
        var modal = $(this);
        modal.find('option[value="'+studentSuperpower+'"]').attr('selected', true);
        submitBtn.attr('data-student-id', studentId);
    });
});
