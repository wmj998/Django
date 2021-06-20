import re
import traceback

from django.core import mail
from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin


class MW(MiddlewareMixin):
    def process_request(self, request):
        print('MW process_request ---')

    def process_view(self, request, callback, callback_args, callback_kwargs):
        print('MW process_view ---')

    def process_response(self, request, response):
        print('MW process_response')
        return response


class VisitLimit(MiddlewareMixin):
    visit_times = {}

    def process_request(self, request):
        ip_address = request.META['REMOTE_ADDR']
        path_url = request.path_info
        if not re.match('^/test', path_url):
            return
        times = self.visit_times.get(ip_address, 0)
        print('%s已访问%d次' % (ip_address, times))
        self.visit_times[ip_address] = times + 1
        if times < 5:
            return
        return HttpResponse('你已访问%d次，被禁止访问' % (times))


class ExceptionMW(MiddlewareMixin):

    def process_exception(self, request, exception):
        error = traceback.format_exc()
        mail.send_mail()
