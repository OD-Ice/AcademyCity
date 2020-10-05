function Register() {
}

Register.prototype.listenImgCaptchaEvent = function () {
    var captchaBtn = $('.img-captcha-btn');
    captchaBtn.click(function () {
        captchaBtn.attr("src", "/acauth/img_captcha/"+"?random="+Math.random());
    });
};

Register.prototype.listenRegisterEvent = function () {
    var registerBtn = $('#register-btn');
    var usernameInput = $('.username-input');
    var telephoneInput = $('.telephone-input');
    var emailInput = $('.email-input');
    var password1Input = $('.password1-input');
    var password2Input = $('.password2-input');
    var captchaInput = $('.captcha-input');
    registerBtn.click(function (event) {
        event.preventDefault();
        var username = usernameInput.val();
        var telephone = telephoneInput.val();
        var email = emailInput.val();
        var password1 = password1Input.val();
        var password2 = password2Input.val();
        var img_captcha = captchaInput.val();
        acajax.post({
            'url': '/acauth/register/',
            'data': {
                'username': username,
                'telephone': telephone,
                'email': email,
                'password1': password1,
                'password2': password2,
                'img_captcha': img_captcha,
            },
            'success': function (result) {
                acalert.alertSuccess({
                    'msg': '注册成功！',
                    'confirmCallback': function () {
                        window.location.reload();
                    }
                });
            }
        });
    });
};

Register.prototype.run = function () {
    this.listenRegisterEvent();
    this.listenImgCaptchaEvent();
};

$(function () {
    var register = new Register();
    register.run();
});