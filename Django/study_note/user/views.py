import csv
import hashlib

from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.http import HttpResponse


# Create your views here.

from user.models import User, Note, Content


def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == 'POST':
        username = request.POST['username']
        if username:
            password_1 = request.POST['password_1']
            password_2 = request.POST['password_2']
            if password_1 and password_2:
                user = User.objects.filter(username=username)
                if user:
                    error = '用户已存在'
                    return render(request, 'register.html', locals())
                else:
                    if password_1 == password_2:
                        try:
                            m = hashlib.md5()
                            m.update(password_1.encode())
                            password_m = m.hexdigest()
                            user_new = User.objects.create(username=username, password=password_m)
                            request.session['username'] = username
                            request.session['id'] = user_new.id
                            return redirect('/show/')
                        except Exception as e:
                            print('---create user error %s' % (e))
                            error = '用户已存在'
                            return render(request, 'register.html', locals())
                    else:
                        error = '您两次输入的密码不一致'
                        return render(request, 'register.html', locals())
            else:
                error = '密码不能为空'
                return render(request, 'register.html', locals())
        else:
            error = '用户名不能为空'
            return render(request, 'register.html', locals())


def login(request):
    if request.method == 'GET':
        s_username = request.session.get('username')
        s_id = request.session.get('id')
        if s_username and s_id:
            return redirect('/show/')
        c_username = request.COOKIES.get('username')
        c_id = request.COOKIES.get('id')
        if c_username and c_id:
            request.session['username'] = c_username
            request.session['id'] = c_id
            return redirect('/show/')
        return render(request, 'login.html')
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if username:
            if password:
                try:
                    m = hashlib.md5()
                    m.update(password.encode())
                    password_m = m.hexdigest()
                    user = User.objects.get(username=username)
                    if password_m == user.password:
                        request.session['username'] = username
                        request.session['id'] = user.id
                        resp = redirect('/show/')
                        if 'remember' in request.POST:
                            resp.set_cookie('username', username, 3600*24*7)
                            resp.set_cookie('id', user.id, 3600*24*7)
                        return resp
                    else:
                        error = '用户名或密码输入错误'
                        return render(request, 'login.html', locals())
                except Exception as e:
                    print('---login error %s' % (e))
                    error = '用户名或密码输入错误'
                    return render(request, 'login.html', locals())
            else:
                error = '请输入密码'
                return render(request, 'login.html', locals())
        else:
            error = '请输入用户名'
            return render(request, 'login.html', locals())


def logout(request):
    if 'username' in request.session:
        del request.session['username']
    if 'id' in request.session:
        del request.session['id']
    resp = redirect('/')
    if 'username' in request.COOKIES:
        resp.delete_cookie('username')
    if 'id' in request.COOKIES:
        resp.delete_cookie('id')
    return resp


def check_login(fun):
    def wrapper(request, *args, **kwargs):
        if 'username' not in request.session or 'id' not in request.session:
            c_username = request.COOKIES.get('username')
            c_id = request.COOKIES.get('id')
            if not c_username or not c_id:
                return redirect('/login/')
        return fun(request, *args, **kwargs)
    return wrapper


@check_login
def add_note(request):
    if request.method == 'GET':
        return render(request, 'add_note.html')
    elif request.method == 'POST':
        id = request.session['id']
        title = request.POST['title']
        content = request.POST['content']
        if title:
            Note.objects.create(title=title, content=content, user_id=id)
            return HttpResponse('保存成功')

        else:
            return HttpResponse('请输入标题')


@check_login
def show_note(request):
    id = request.session['id']
    notes = Note.objects.filter(user_id=id)
    return render(request, 'user.html', locals())


def test(request):
    print('MW ---')
    return HttpResponse('MV ---')


def page(request):
    page_num = request.GET.get('page', 1)
    data_list = ['a', 'b', 'c', 'd', 'e', 'f']
    paginator = Paginator(data_list, 2)
    now_page = paginator.page(int(page_num))
    return render(request, 'page.html', locals())


def download(request):
    page_num = request.GET.get('page', 1)
    data_list = ['a', 'b', 'c', 'd', 'e', 'f']
    paginator = Paginator(data_list, 2)
    now_page = paginator.page(int(page_num))

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="page-%s.csv"' % (page_num)
    writer = csv.writer(response)
    for content in now_page:
        writer.writerow(content)
    return response


def upload(request):
    if request.method == 'GET':
        return render(request, 'upload.html')
    elif request.method == 'POST':
        now_file = request.FILES['file']
        Content.objects.create(file=now_file)

        return HttpResponse('上传成功')


@check_login
def delete(request):
    id = request.GET.get('id')
    note = Note.objects.filter(id=id)
    note.delete()
    return redirect('/show/')


@check_login
def update(request):
    if request.method == 'GET':
        id = request.GET.get('id')
        note = Note.objects.get(id=id)
        title = note.title
        content = note.content
        create_time = note.create_time
        update_time = note.update_time
        return render(request, 'update.html', locals())
    elif request.method == 'POST':
        id = request.GET.get('id')
        title = request.POST['title']
        content = request.POST['content']
        note = Note.objects.get(id=id)
        note.title = title
        note.content = content
        note.save()
        return redirect('/show/')


