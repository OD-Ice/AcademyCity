from django.shortcuts import reverse


class ACLogin:
    def __init__(self, get_response):
        # 执行一些初始化代码
        self.get_response = get_response

    def __call__(self, request):
        if request.path_info != reverse('acauth:login') and request.path_info != reverse('acauth:register') and request.path_info != reverse('acauth:img_captcha'):
            if not hasattr(request, 'user') or not request.user.is_authenticated:
                request.path_info = reverse('acauth:login')

        response = self.get_response(request)
        return response
