from django.http import JsonResponse
def allow_origin(func):
    def _func(*args, **kwargs):
        data = func(*args, **kwargs)
        response = JsonResponse(data)
        response['Access-Control-Allow-Origin'] = '*'
        return response
    return _func