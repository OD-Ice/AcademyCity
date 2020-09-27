function StudentList() {

}

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
};

$(function () {
    var student_list = new StudentList();
    student_list.run();
});
