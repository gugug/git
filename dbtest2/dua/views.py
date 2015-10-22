#coding=utf-8
from django.shortcuts import render,render_to_response
from dua.models import *
from django import forms
from django.contrib.auth import authenticate as au, login,logout
from django.http import HttpResponseRedirect, HttpResponse,Http404
from django.template.context import RequestContext
from sina.class_mysql_uid import *

#json:dump(s)--把xx打包为json,load(s)--把json解压为xx;字典类型不能传输




class UserForm(forms.Form):    # 登陆页面用户表单
    username = forms.CharField(label='用户名：',  error_messages={'required': '请输入用户名'}, max_length=50)
    password = forms.CharField(label='密码：', error_messages={'required': '请输入密码'}, widget=forms.PasswordInput())

def login_page(request):
    if request.user.is_authenticated():
        return render_to_response('index.html', RequestContext(request,{'existed':True}))
    if request.method == "POST":
        uf = UserForm(request.POST)
        try:
            uf.is_valid()
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            user = au(username=username, password=password)
            if user is not None:  #au:如果正确返回User对象,否则返回None
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/main_page/%s' % user.username)
            else:
                    return render_to_response('login.html',{'wrong':True})
        except Exception,e: #某一项为空都会转到这里
            print e
            # return render_to_response('login.html', RequestContext(request, {'wrong': True}))
    else: #非登录用户会到回到登录页
        return render_to_response('login.html')

def show_database(request,id):
    try:
        user=SinaUser.objects.get(pk=id)
        fans=GDFan.objects.order_by('gdfans_id')
        follows=GDFollow.objects.order_by('gdfollows_id')
        weibo=WeiboText.objects.order_by('time')
        content={'user':user,'fans':fans,'follows':follows,'weibo':weibo}
    except:
        raise Http404("Question does not exist")
    return render_to_response('showdb.html',content)

def index(request):
    if request.user.is_authenticated():
        return render_to_response('index.html', RequestContext(request,{'success':True}))
    else:
        return render_to_response('index.html',{'success':False})

class RegisterForm(forms.Form):
    # email=forms.EmailField(max_length=50,label='邮箱',error_messages={'required':'请输入邮箱'})
    username1=forms.CharField(max_length=50,label='用户名',error_messages={'required':'请输入用户名'})
    pwd3=forms.CharField(max_length=50,label='密码',error_messages={'required':'请输入密码'})
    pwd2=forms.CharField(max_length=50,label='密码',error_messages={'required':'请再次输入密码'})


def register_page(request): #9.2:js2可以连接到这个函数,表单名pwd3,pwd2这些修改无效,只能跟着js命名
    if request.method=='POST':
        rf=RegisterForm(request.POST)
        try:
            print request.POST
            a=rf.is_valid() #填入表单
            print 'a',a
            print rf.cleaned_data
            # email=rf.cleaned_data['email']
            username=rf.cleaned_data['username1']
            password1=rf.cleaned_data['pwd3']
            password2=rf.cleaned_data['pwd2']
            tmp=MyUser.objects.exclude(pk=request.user.pk)
            # if tmp.filter(email=email).exists(): #
            #     return render_to_response('register.html',RequestContext(request,{'registered_email':True}))
            if tmp.filter(name=username).exists():  #用户名判重
                return render_to_response('register.html',RequestContext(request,{'registered_name':True}))
            else:
                MyUser.objects.create(name=username,password=password1)
            return HttpResponseRedirect('/index')
        except (ValueError,KeyError),e:
            print e
            return render_to_response('errors.html',RequestContext(request,{'registered':True}))
    else:
        rf=RegisterForm()
        return render_to_response('index.html',RequestContext(request,{'existed':False}))

def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/login')

def main_page(request):
    # if request.user.is_authenticated():
    #     return render_to_response('main_page.html', RequestContext(request,{'existed':True}))
    # if request.method == "POST":
    #     uf = UserForm(request.POST)
    #     if uf.is_valid():
    #         username = uf.cleaned_data['username']
    #         password = uf.cleaned_data['password']
    #         user = au(username=username, password=password)
    #         if user is not None:  #au:如果正确返回User对象,否则返回None
    #             if user.is_active:
    #                 login(request, user)
    #                 return HttpResponseRedirect('/main_page/%s' % user.username)
    #         else:
    #                 return render_to_response('login.html',{'wrong':True})
    #     else: #某一项为空都会转到这里
    #         return render_to_response('login.html', RequestContext(request, {'wrong': True}))
    # else:
    #     return HttpResponseRedirect('main_page.html')
    return render(request,'main_page.html')

def get_id(request):
    db=Database()
    user_list = db.get_mysql_user()
    dict_uid=dict()
    dict_uid['user_id']=user_list
    post_data=json.dumps(dict_uid)
    return HttpResponse(post_data)