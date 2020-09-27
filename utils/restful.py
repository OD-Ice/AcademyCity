from django.http import JsonResponse


class HttpCode:
    ok = 200
    paramserror = 400
    unauth = 401
    methoderror = 405
    servererror = 500


# {"code": 200, "message": "", "data": {}}
def result(code=HttpCode.ok, message='', data=None, kwargs=None):
    json_dict = {'code': code, 'message': message, 'data': data}
    # 存在kwargs并且是个字典并且是有值的
    if kwargs and isinstance(kwargs, dict) and kwargs.keys():
        json_dict.update(kwargs)
    return JsonResponse(json_dict)


def ok():
    return result()


def params_error(message="", data=None):
    return result(code=HttpCode.paramserror, message=message, data=data)


def unauth(message="", data=None):
    return result(code=HttpCode.unauth, message=message, data=data)


def methoderror(message="", data=None):
    return result(code=HttpCode.methoderror, message=message, data=data)


def servererror(message="", data=None):
    return result(code=HttpCode.servererror, message=message, data=data)
