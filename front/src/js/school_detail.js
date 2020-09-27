function SchoolDetail() {

}

SchoolDetail.prototype.listenJoinEvent = function () {
    var joinBtn = $('.join-btn');
    joinBtn.click(function () {
        var schoolId = $(this).attr('data-school-id');
        var schoolName = $(this).attr('data-school-name');
        acajax.post({
            'url': '/join_school/',
            'data': {
                'school_id': schoolId
            },
            'success': function (result) {
                acalert.alertSuccess({
                    'msg': '欢迎加入'+schoolName+'!',
                    'confirmCallback': function () {
                        window.location.reload();
                    }
                });
            }
        });
    });
};

SchoolDetail.prototype.listenQuitEvent = function () {
    var quitBtn = $('.quit-btn');
    quitBtn.click(function () {
        var schoolName = $(this).attr('data-school-name');
        acalert.alertConfirm({
            'msg': '确定要退出'+schoolName+'吗？',
            'confirmCallback': function () {
                acajax.post({
                    'url': '/quit_school/',
                    'data':{},
                    'success': function (result) {
                        acalert.alertSuccess({
                            'title': '欧耶~',
                            'msg': '恭喜你成功辍学！',
                            'confirmCallback': function () {
                                window.location.reload();
                            }
                        });
                    }
                });
            }
        });
    });
};

SchoolDetail.prototype.listenCommentEvent = function () {
    var submitBtn = $('.submit-btn');
    var commentInput = $('#comment');
    submitBtn.click(function () {
        var content = commentInput.val();
        var schoolId = $(this).attr('data-school-id');
        acajax.post({
            'url': '/add_comment/',
            'data': {
                'content': content,
                'school_id': schoolId
            },
            'success': function (result) {
                acalert.alertSuccess({
                    'msg': '评论发布成功！',
                    'confirmCallback': function () {
                        window.location.reload();
                    }
                });
            }
        });
    });
};

SchoolDetail.prototype.run = function () {
    this.listenJoinEvent();
    this.listenQuitEvent();
    this.listenCommentEvent();
};

$(function () {
    var school_detail = new SchoolDetail();
    school_detail.run();
});
