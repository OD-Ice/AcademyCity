function Index() {

}

Index.prototype.applyLevel = function () {
    var applyLevelBtn = $('.level-msg-btn');
    var levelInput = $('#level-input');
    applyLevelBtn.click(function () {
        var levelId = levelInput.val();
        acajax.post({
            'url': '/add_message/',
            'data': {
                'type': 'apply_level',
                'level_id': levelId,
            },
            'success': function (result) {
                window.location.reload();
            }
        });
    });
};

Index.prototype.applyDirector = function () {
    var applyDirectorBtn = $('.apply-director');
    applyDirectorBtn.click(function () {
        acajax.post({
            'url': '/add_message/',
            'data': {
                'type': 'apply_director'
            },
            'success': function (result) {
                window.location.reload();
            }
        });
    });
};

Index.prototype.agreeApplyLevel = function () {
    var agreeBtn = $('.agree_apply_level');
    agreeBtn.click(function () {
        var sponsor_id = $(this).attr('data-sponsor');
        var level_id = $(this).attr('data-level');
        var message_id = $(this).attr('data-message-id');
        acajax.post({
            'url': '/agree_apply_level/',
            'data': {
                'sponsor_id': sponsor_id,
                'level_id': level_id,
                'message_id': message_id,
            },
            'success': function (result) {
                window.location.reload();
            }
        });
    });
};

Index.prototype.agreeApplyDirector = function () {
    var agreeBtn = $('.agree_apply_director');
    agreeBtn.click(function () {
        var sponsor_id = $(this).attr('data-sponsor');
        var message_id = $(this).attr('data-message-id');
        acajax.post({
            'url': '/agree_apply_director/',
            'data': {
                'sponsor_id': sponsor_id,
                'message_id': message_id,
            },
            'success': function (result) {
                window.location.reload();
            }
        });
    });
};

Index.prototype.delMessage = function () {
    var delBtn = $('.del-message');
    delBtn.click(function () {
        var messageId = $(this).attr('data-message-id');
        acajax.post({
            'url': '/del_message/',
            'data': {
                'message_id': messageId,
            },
            'success': function (result) {
                window.location.reload();
            }
        });
    });
};

Index.prototype.uploadAvatar = function () {
    var img = $('.avatar-img');
    var avatarInput = $('.avatar-input');
    img.click(function () {
        avatarInput.click();
        avatarInput.change(function () {
            var file = avatarInput[0].files[0];
            var formData = new FormData();
            formData.append('file', file);
            acajax.post({
                'url': '/acauth/upload_avatar/',
                'data': formData,
                'processData': false,   // 告诉jQuery这是个文件，不需要再进行处理
                'contentType': false,   // 不需要再添加数据类型，默认文件格式就行
                'success': function (result) {
                    window.location.reload();
                }
            });
        });
    });
};

Index.prototype.run = function () {
    this.uploadAvatar();
    this.applyLevel();
    this.agreeApplyLevel();
    this.delMessage();
    this.applyDirector();
    this.agreeApplyDirector();
};

$(function () {
    var index = new Index();
    index.run();

    // Donut Chart
    var donutChartCanvas = $('#donutChart').get(0).getContext('2d');
    var labels = jQuery.parseJSON($(donutChartCanvas['canvas']).attr('data-labels'));
    var counts = jQuery.parseJSON($(donutChartCanvas['canvas']).attr('data-counts'));

    var donutData = {
        labels: labels,
        datasets: [
            {
                data: counts,
                backgroundColor: ['#f56954', '#00a65a', '#f39c12', '#00c0ef', '#3c8dbc', '#d2d6de', '#FFFF33'],
            }
        ]
    }
    var donutOptions = {
        maintainAspectRatio: false,
        responsive: true,
    }

    var donutChart = new Chart(donutChartCanvas, {
        type: 'doughnut',
        data: donutData,
        options: donutOptions
    });
});
