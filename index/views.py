import csv

from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render

from BookStore import settings
from index.models import Book

#方式一
# from django.template import loader # 导入loader方法
# def test_html(request):
#     t=loader.get_template('test.html')
#     html=t.render({'name':'c语言中文网'})#以字典形式传递数据并生成html
#     return HttpResponse(html) #以 HttpResponse方式响应html

#方式二
from django.shortcuts import render #导入render 方法
from django.urls import reverse


from django.core.signals import request_started, request_finished
from django.dispatch.dispatcher import receiver
@receiver(request_started)
def request_started_callback(sender, **kwargs):
    print('请求开始')

@receiver(request_finished)
def request_finished_callback(sender, **kwargs):
    print('请求完成')



def test_html(request, id):
    a={} #创建空字典，模板必须以字典的形式进行传参
    a['name']='C语言中文网'
    a['course']=["Python","C","C++","Java"]
    a['b']={'name':'C语言中文网','address':'http://c.biancheng.net/'}
    a['test_hello']=test_hello
    a['class_obj']=Website()
    a['x'] = 5
    a['sense'] = 'you are a hero'
    a['value'] = [
                    {'name': 'C语言中文网', 'num': 2},
                    {'name': 'Django官网', 'num': 1},
                    {'name': 'Django官网', 'num': 4},
                    {'name': 'Python官网', 'num': 3},
                ]
    a['id'] = id

    if id == 3:
        return render(request, 'test3.html', a)
    elif id == 4:
        return render(request, 'test4.html', {'variable':'Hhhhello'})
    else:
        return render(request,'test.html',a)

def test_hello():
    return '欢迎来到C语言中文网'

class Website:
    def Web_name(self):
        return 'Hello，C语言中文网!'
    Web_name.alters_data=True #不让Website()方法被模板调用

def test2(request):
    return render(request, 'test2.html')

def base_html(request):
    return render(request, 'base.html')

def ext1_html(request):
    return render(request, 'ext1.html', {'name':'zhou', 'course':['aa', 'bb', 'cc']})

def filter1_html(request):
    return render(request, 'filter1.html', {'str1':'abc django Django', 'list1':[
        {'key3':1}, {'key2':2}, {'key1':3}
    ]})

def redict_url(request):
    return render(request, 'redict.html')

def redict2_url(request):
    return render(request, 'redict2.html')

#reverse函数实现反向解析重定向到我们想要的有页面
def test_to_reverse(request):
    return HttpResponseRedirect(reverse('index:redict2', current_app=request.resolver_match.namespace))

def image_html(request, img):
    return render(request, 'img.html', {'img':img})

from django.db import connection

def showbook(request, bookname):
    with connection.cursor() as cur:
        cur.execute('update index_author set name="upd name2" where id=1')

    sql = 'select * from index_book where title = %s'
    books = Book.objects.raw(sql, [bookname])
    return render(request, 'books.html', {'books':books})


from index.forms import LoginForm
def login(request):
    form = LoginForm()
    return render(request, 'login.html', locals())


from django.views import View
class IndexC(View):
    def test10(self, request):
        return render(request, 'test10.html')

    def get(self, request):
        str1 = request.path + '|' + request.method + '|' + request.get_host()\
            + "request.META('REMOTE_ADDR')"
        return HttpResponse(str1)

    def post(self, request):
        pass

from index.forms import LoginForm
#第二步围绕form对象完成表单。
def login2(request):#定义登录处理函数login()
    if request.method == "POST": #request是 HttpRequest的对象，利用它的的method属性，判断请求方法。
        form = LoginForm(request.POST)#实例化对象，post提交数据是QuerySet类型的字典，GET方法与其一样。
        if form.is_valid(): #提供验证判断是否有效，成立则返回是Ture
            return HttpResponse("登录成功")
    else:
        form=LoginForm()
    return render(request, "test10.html",locals())


#设置添加cookie
def set_cookie_view(request):
    resp=HttpResponse()
    resp.set_cookie('username','cbiancheng',3600)
    return resp

#得到cookie的值使用get方法
def get_cookie_view(request):
    value = request.COOKIES.get('username')
    return HttpResponse('--MY COOKIE is--%s'%value)


from index.models import UserInfo
import hashlib
#用户的登录逻辑处理
def login3(request):
    #处理GET请求
    if request.method == 'GET':
        #1, 首先检查session，判断用户是否第一次登录，如果不是，则直接重定向到首页
        # if 'username' in request.session:  #request.session 类字典对象
        #     # return HttpResponseRedirect('/index/allbook')
        #     return HttpResponse("登录成功1")
        # #2, 然后检查cookie，是否保存了用户登录信息
        # if 'username' in request.COOKIES:
        #     #若存在则赋值回session，并重定向到首页
        #     request.session['username'] = request.COOKIES['username']
        #     # return HttpResponseRedirect('/index/allbook')
        #     return HttpResponse("登录成功2")
        #不存在则重定向登录页，让用户登录
        return render(request, 'login3.html')
    # 处理POST请求
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        m = hashlib.md5()
        m.update(password.encode())
        password_m = m.hexdigest()
        #判断输入是否其中一项为空或者格式不正确
        if not username or not password:
            error = '你输入的用户名或者密码错误 !'
            return render(request, 'login3.html', locals())
        #若输入没有问题则进入数据比对阶段，看看已经注册的用户中是否存在该用户
        users = UserInfo.objects.filter(username=username, password=password)
        # 由于使用了filter, 所以返回值user是一个数组，但是也要考虑其为空的状态，即没有查到该用户
        if not users:
            error = '用户不存在或用户密码输入错误!!'
            return render(request, 'login3.html', locals())
        # 返回值是个数组，并且用户名具备唯一索引，当前用户是该数组中第一个元素
        users = users[0]
        request.session['username'] = username

        #response = HttpResponseRedirect('/index/allbook')
        response = HttpResponse("登录成功3. <a href='logout'>退出</a>")
        if 'isSaved' in request.POST.keys():
            response.set_cookie('username', username, 60 * 60 * 24 * 7)
        return response

def logout(request):
    #实现退出功能
    #删除session
    if 'username' in request.session:
        del request.session['username']
    # resp = HttpResponseRedirect('/user/index')
    resp = HttpResponse('退出成功')
    #删除cookie
    if 'username' in request.COOKIES:
        resp.delete_cookie('username')

    return resp

from index.forms import BookSearch

from django.contrib.auth.decorators import login_required
@login_required
def book_search(request):
    booksearchform = BookSearch()
    return render(request, 'booksearch.html', locals())

from index.signal import book_search_signal
def book_search_result(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        public = request.POST.get('public')
        author = request.POST.get('author')

        try:
            # booklist = Book.objects.filter(title__contains=title)
            booklist = Book.objects.filter(title__contains=title, public__name__contains=public)
            # booklist = booklist.author_set.filter(name__contains=author).books.all()
        except Exception as e:
            pass

        if booklist:
            pass

        book_search_signal.send(book_search_result, request=request, book=booklist[0])
        return render(request, 'booksearchresult.html', locals())

def book_table(request):
    print(request.method)
    if request.method == 'GET':
        return render(request, 'book_table.html', locals())
    elif request.method == 'POST':
        book_name = request.POST.get('book_name')
        if book_name:       # 查询书籍
            booklist = Book.objects.filter(title__contains=book_name)
            return render(request, 'book_table.html', locals())

    return HttpResponse('查询出错')

from index.forms import PubForm
from index.models import Pub
def pub_search(request):
    print(request.method)

    if request.method == 'GET':
        pub_form = PubForm(request.GET)
        print(pub_form)
        if pub_form.is_valid():
            pub_list = Pub.objects.filter(name__contains=pub_form.cleaned_data['name'],
                                          addr__contains=pub_form.cleaned_data['addr'])
            print(pub_list)
            return render(request, 'pub_search.html', {'pub_list':pub_list})

        else:
            return render(request, 'pub_search.html', {'pub_form' : PubForm()})
    elif request.method == 'POST':
        pass
    return HttpResponse('网址错误1')

from index.forms import UserInfoForm
def userinfo_register(request):
    print(request.method)
    if request.method == 'GET':
        return render(request, 'userinfoadd.html', {'userinfoform':UserInfoForm()})
    elif request.method == 'POST':
        uif = UserInfoForm(request.POST)
        print(uif.is_valid())
        return HttpResponse('测试中')


from django.core.paginator import *
def book_page(request):
    """ 接受页面传递参数page，传递all books的第page页数据 """
    book_list = Book.objects.all()
    page_num = request.GET.get('page', 1)
    pt = Paginator(book_list, 3)
    page = pt.page(page_num)
    return render(request, 'book_page.html', locals())

def welcome(request):
    return render(request, 'welcome.html')

import os
def upload(request):
    if request.method == 'GET':
        return render(request, 'index/upload.html')
    elif request.method == 'POST':
        # 使用request.FILES['myfile']获得文件流对象file
        # file = request.FILES['myfile']
        files = request.FILES.getlist('myfile')
        # 文件储存路径，应用settings中的配置，file.name获取文件名
        for file in files:
            filename = os.path.join(settings.MEDIA_ROOT, file.name)
            # 写文件
            with open(filename, 'wb') as f:
                # file.file 获取文件字节流数据
                data = file.file.read()
                f.write(data)
        return HttpResponse('成功保存了 %s 文件' % (file.name))

    return HttpResponse("upload未获取")

def downloadcsv(request):
    return render(request, 'index/downloadcsv.html')

def downloadcsv2(request):
    # 生成csv文本
    # 生成response的content-type头
    res = HttpResponse(content_type='text/csv')
    # 固定格式,添加 content-Disposition头，设置以附件方式下载，并给文件添加默认文件名
    res['Content-Disposition'] = 'attachment;filename="allUser.csv"'
    # 获取数据库中数据
    users = UserInfo.objects.all()
    # 生成writer的写对象
    writer = csv.writer(res)
    # 写csv表头，即想要展示字段名
    writer.writerow(['username', 'password'])
    # 写具体数据
    for user in users:
        writer.writerow([user.username, user.password])
    return res


