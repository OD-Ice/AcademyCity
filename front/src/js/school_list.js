function SchoolList() {
}

SchoolList.prototype.listenDelEvent = function () {
    var delBtn = $('.del-btn');
    delBtn.click(function () {
        console.log('1');
        var self = this;
        acalert.alertConfirm({
            'msg': '确定要删除此学校吗？',
            'confirmCallback': function () {
                var schoolId = $(self).attr('data-school-id');
                acajax.post({
                    'url': '/del_school/',
                    'data': {
                        'school_id': schoolId
                    },
                    'success': function (result) {
                        acalert.alertSuccess({
                            'msg': '删除成功！',
                            'confirmCallback': function () {
                                window.location.reload();
                            }
                        })
                    }
                })
            }
        })
    });
};

SchoolList.prototype.run = function () {
    this.listenDelEvent();
};

$(function () {
    var schoolList = new SchoolList();
    schoolList.run();
});
