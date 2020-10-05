var acalert = {
    /*
    功能：错误提示
    参数：
        - msg：提示的内容(可选)
     */
    'alertError': function (msg) {
        swal('提示', msg, 'error');
    },
    /*
    功能：信息提示
    参数：
        - msg：提示的内容(可选)
     */
    'alertInfo': function (msg) {
        swal('提示', msg, 'warning');
    },
    /*
    功能：可自定义标题的信息提示
    参数：
        - title：标题
        - msg：提示的内容(可选)
     */
    'alertInfoWithTitle': function (args) {
        swal(args['title'], args['msg']);
    },
    /*
    功能：成功的提示
    参数：
        - msg：提示的内容(必选)
        - confirmCallback：确认按钮的执行事件(可选)
     */
    'alertSuccess': function (args) {
        var title = '恭喜！';
        if (args['title']) {
            title = args['title'];
        }
        swal({
            title: title,
            text: args['msg'],
            icon: 'success'
        })
        .then(function(is_confirm) {
            if (is_confirm) {
                args['confirmCallback']();
            }
        });
    },
    /*
    功能：一个输入框
    参数：
        - text：提示的内容(必选)
        - confirm_text：确认按钮提示内容
        - placeholder: 输入框中的内容
        - confirmCallback：确认按钮的执行事件(可选)
     */
    'alertOneInput': function (args) {
        swal({
            text: args['text'],
            content: {
                element: "input",
                attributes: {
                placeholder: args['placeholder'] ? args['placeholder']: ''
                }
            },
            buttons: args['confirm_text']
        })
        .then(function (inputValue) {
            if (!inputValue) throw null;
            args['confirmCallback'](inputValue);
        })
        .catch(function (err) {
            if (err) {
                swal("出错啦！", "The AJAX request failed!", "error");
            } else {
                swal.stopLoading();
                swal.close();
            }
        });
    },
    /*
    功能：确认操作
    参数：
        - text：提示的内容(必选)
        - confirmCallback：确认按钮的执行事件
    */
    'alertConfirm': function (args) {
        swal({
            title: '警告',
            text: args['msg'],
            icon: 'warning',
            buttons: ['取消', '确定'],
            dangerMode: true
        })
        .then(function(is_confirm) {
            if (is_confirm) {
                args['confirmCallback']();
            }
        });
    }
};