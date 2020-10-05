function AddSchool() {

}

AddSchool.prototype.uploadBadge = function () {
    var uploadBtn = $('#school-badge');
    uploadBtn.change(function () {
        var file = uploadBtn[0].files[0];
        var formData = new FormData();
        formData.append('file', file);
        acajax.post({
            'url': '/upload_badge/',
            'data': formData,
            'processData': false,   // 告诉jQuery这是个文件，不需要再进行处理
            'contentType': false,   // 不需要再添加数据类型，默认文件格式就行
            'success': function (result) {
                var url = result['data']['url'];
                    var file_label = $('.custom-file-label');
                    file_label.html(url);
            }
        });
    });
};

AddSchool.prototype.listenAddEvent = function () {
    var submitBtn = $('#submit-btn');
    var nameInput = $('#school-name');
    var levelInput = $('#school-level');
    var categoryInput = $('#school-category');
    var superInput = $('#super');
    var badgeInput = $('.custom-file-label');
    var locationInput = $('#school-location');
    var emailInput = $('#school-email');
    var courseInput = $('#school-course');
    submitBtn.click(function () {
        var name = nameInput.val();
        var school_level = levelInput.val();
        var school_category = categoryInput.val();
        var is_super = null;
        is_super = superInput.val() === '1';
        var school_badge = badgeInput.html();
        var location = locationInput.val();
        var email = emailInput.val();
        var course_des = courseInput.val();
        var desc = tinyMCE.activeEditor.getContent();
        var school_id = $(this).attr('data-school-id');
        var url = null;
        var msg = null;
        if (school_id) {
            url = '/edit_school/';
            msg = '修改成功！';
        } else {
            url = '/add_school/';
            msg = '注册成功！';
        }
        acajax.post({
            'url': url,
            'data': {
                'name': name,
                'school_level': school_level,
                'school_category': school_category,
                'is_super': is_super,
                'school_badge': school_badge,
                'location': location,
                'email': email,
                'course_des': course_des,
                'desc': desc,
                'school_id': school_id
            },
            'success': function (result) {
                acalert.alertSuccess({
                    'msg': msg,
                    'confirmCallback': function () {
                        window.location.href = '/school_list/';
                    }
                });
            }
        });
    });
}

AddSchool.prototype.run = function () {
    this.uploadBadge();
    this.listenAddEvent();
};

$(function () {
    var add_school = new AddSchool();
    add_school.run();
});