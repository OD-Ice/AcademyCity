function Login() {
}

Login.prototype.listenLoginEvent = function () {
    var loginBtn = $('#login-btn');
    loginBtn.click(function (event) {
        event.preventDefault();
        var telephone = $('.telephone').val();
        var password = $('.password').val();
        var remember = $('#remember').prop('checked');
        acajax.post({
            'url': '/acauth/login/',
            'data': {
                'telephone': telephone,
                'password': password,
                'remember': remember,
            },
            'success': function (result) {
                window.location.replace("/");
            }
        });
    });
};

Login.prototype.run = function () {
    this.listenLoginEvent();
};

$(function () {
    var login = new Login();
    login.run();
});
