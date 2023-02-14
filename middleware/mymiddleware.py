import time

from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin

ip_pool = {}

class MyMiddleWare(MiddlewareMixin):
    def process_request(self, request):
        print("中间件方法 process_request 被调用", ip_pool)
        # 限制用户访问次数,每5秒不超过3次
        newip = request.META.get('REMOTE_ADDR')
        visit_time = time.time()

        if newip not in ip_pool:
            ip_pool[newip] = [visit_time]
            return None
        else:
            ip_list = ip_pool[newip]
            if len(ip_list) == 3:
                if visit_time - ip_list[-1] > 5:
                    ip_list.pop()
                    ip_list.insert(0, visit_time)
                    return None
                else:
                    return HttpResponse('访问太过频繁，请稍后再访问')
            else:
                ip_list.insert(0, visit_time)

        # ip_list = ip_pool[newip]
        # if ip_list[0] - ip_list[-1] > 5:
        #     ip_list.pop()
        #
        # if len(ip_list) > 3:
        #     print(ip_pool[newip])
        #     return HttpResponse('访问太过频繁，请稍后再访问')


        

    def process_view(self, request, callback, callback_args, callback_kwargs):
        print("中间件方法 process_view 被调用")

    def process_response(self, request, response):
        print("中间件方法 process_response 被调用")
        return response

    def process_exception(self, request, exception):
        print("中间件方法 process_exception 被调用")

    def process_template_response(self, request, response):
        print("中间件方法 process_template_response 被调用")
        return response