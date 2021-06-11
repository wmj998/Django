from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


def h(request):
    method = request.method
    path = request.path
    return HttpResponse(method)


def j(request):
    info = {'name': 'Tom', 'age': 20}
    return JsonResponse(info)


def l(request):
    info = ['name', 'age']
    user = {'info': info}
    return render(request, 'l.html', user)


def d(request):
    user = {'info': {'name': 'Tom', 'age': 20}}
    return render(request, 'd.html', user)


def c(request):
    class People(object):
        def __init__(self, name):
            self.name = name
    ren = People('Tom')
    user = {'info': ren}
    return render(request, 'c.html', user)


def index(request):
    number = dict(zip('abcde', range(1, 6)))
    return render(request, 'index.html', {'dict': number})
