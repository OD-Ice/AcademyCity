function Index() {

}

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
};

$(function () {
    var index = new Index();
    index.run();
});
