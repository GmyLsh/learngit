"""
通过自定义的手段来实现后台获取接口版本号，也可以使用drf内置的类实现。如果使用内置的类，直接REST_FRAMEWORK配置中，配置成内置类即可。
"""

from rest_framework.versioning import BaseVersioning

class Version(BaseVersioning):
    #determine:确定，确认
    def determine_version(self, request, *args, **kwargs):
        #获取此次请求的版本号
        #query_params:查询字符串
        version=request.query_params.get('version')
        return version
