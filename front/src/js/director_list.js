function DirectorList() {

}

DirectorList.prototype.listenDelEvent = function () {
    var delBtn = $('.del-btn');
    delBtn.click(function (event) {
        event.preventDefault();
        var director_id = $(this).attr('data-director-id');
        var director_name = $(this).attr('data-director-name');
        acalert.alertConfirm({
            'msg': '确定要开除'+director_name+'吗?',
            'confirmCallback': function () {
                acajax.post({
                    'url': '/del_director/',
                    'data': {
                        'director_id': director_id
                    },
                    'success': function (result) {
                        acalert.alertSuccess({
                            'title': '欧耶~',
                            'msg': '恭喜你炒了'+director_name+'！TA要喝西北风了！',
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

DirectorList.prototype.run = function () {
    this.listenDelEvent();
};

$(function () {
    var director_list = new DirectorList();
    director_list.run();
});
