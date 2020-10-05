from django.conf import settings
from utils import restful
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import os


@csrf_exempt  # 防止post时引发403错误
def upload_view(request):
    if request.method == 'POST':
        f = request.FILES.get('file')
        name = f.name
        path = os.path.join(settings.MEDIA_ROOT, name)

        with open(path, 'wb') as fp:
            for chunk in f.chunks():
                fp.write(chunk)
        return JsonResponse({
            'location': settings.MEDIA_URL + name
        })
    else:
        return restful.methoderror('请求方式错误！')
