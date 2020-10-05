function Level() {

}

Level.prototype.listenSubmitBtn = function () {
    var submitBtn = $('.submit-btn');
    var levelInput = $('#level-input');
    var priorityInput = $('#priority-input');
    submitBtn.click(function () {
        var levelName = levelInput.val();
        var priority = priorityInput.val();
        var levelId = $(this).attr('data-id');
        var url = null;
        var msg = null;
        if (levelId) {
            url = '/edit_school_level/';
            msg = '修改成功！'
        } else {
            url = '/add_school_level/';
            msg = '添加成功！'
        }
        acajax.post({
            'url': url,
            'data': {
                'name': levelName,
                'priority': priority,
                'level_id': levelId,
            },
            'success': function (result) {
                acalert.alertSuccess({
                    'msg': msg,
                    'confirmCallback': function () {
                        window.location.reload();
                    }
                });
            }
        });
    });
};

Level.prototype.listenDelBtn = function () {
    var delBtn = $('.delete-btn');
    delBtn.click(function () {
        var self = this;
        acalert.alertConfirm({
            'msg': '确定要删除此科研等级吗？',
            'confirmCallback': function () {
                var levelId = $(self).attr('data-id');
                acajax.post({
                    'url': '/del_school_level/',
                    'data': {
                        'level_id': levelId
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

Level.prototype.run = function () {
    this.listenSubmitBtn();
    this.listenDelBtn();
};


$(function () {
    var level = new Level();
    level.run();

    $('#level-modal').on('show.bs.modal', function (event) {
        var button = $(event.relatedTarget); // Button that triggered the modal
        var level = button.data('level');
        var priority = parseInt(button.data('priority'));
        var levelId = button.data('id');// Extract info from data-* attributes
        // If necessary, you could initiate an AJAX request here (and then do the updating in a callback).
        // Update the modal's content. We'll use jQuery here, but you could use a data binding library or other methods instead.
        var modal = $(this);
        modal.find('.modal-body #level-input').val(level);
        modal.find('.modal-body #priority-input').val(priority);
        if (levelId) {
            modal.find('.modal-footer .submit-btn').attr('data-id', levelId);
        } else {
            modal.find('.modal-footer .submit-btn').removeAttr('data-id');
        }
    });
});