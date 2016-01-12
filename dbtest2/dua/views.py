# coding=utf-8
from django.shortcuts import render, render_to_response
from dua.models import *
from django import forms
from django.contrib.auth import authenticate as au, login, logout
from django.http import HttpResponseRedirect, HttpResponse, Http404,JsonResponse
from django.template.context import RequestContext
from sina.class_mysql_uid import *
from sina.class_page import *
import json
# json:dump(s)--把xx打包为json,load(s)--把json解压为xx;字典类型不能传输



class UserForm(forms.Form):  # 登陆页面用户表单
    username = forms.CharField(label='用户名：', error_messages={'required': '请输入用户名'}, max_length=50)
    password = forms.CharField(label='密码：', error_messages={'required': '请输入密码'}, widget=forms.PasswordInput())


def login_page(request):
    if request.user.is_authenticated():  # 判断用户是否已经登录
        print 'aa'
        message = '你已经登陆'
        back = '/main_page/'
        return render_to_response('redirect.html', {'message': message, 'back':back})
    if request.method == "POST":
        uf = UserForm(request.POST)
        if uf.is_valid():
            try:
                username = uf.cleaned_data['username']
                password = uf.cleaned_data['password']
                user = au(username=username, password=password)
                # print username
                # print password
                if user is not None:  # au:如果正确返回User对象,否则返回None
                    if user.is_active:
                        login(request, user)
                        return HttpResponseRedirect('/main_page/%s' % user.username)
                    else:
                        print "你的帐号不能用"
                else:
                    return render_to_response('home.html', {'wrong': True})
            except Exception, e:  # 某一项为空都会转到这里
                print e
                # return render_to_response('login.html', RequestContext(request, {'wrong': True}))
        else:
            print "不合法填写表单"
            return render_to_response('home.html')
    else:  # 非登录用户会到回到登录页
        return render_to_response('home.html')


def show_database(request, id):
    try:
        user = SinaUser.objects.get(pk=id)
        fans = GDFan.objects.order_by('gdfans_id')
        follows = GDFollow.objects.order_by('gdfollows_id')
        weibo = WeiboText.objects.order_by('time')
        content = {'user': user, 'fans': fans, 'follows': follows, 'weibo': weibo}
    except:
        raise Http404("Question does not exist")
    return render_to_response('home.html', content)


def index(request):
    if request.user.is_authenticated():
        return render_to_response('index.html', RequestContext(request, {'success': True}))
    else:
        return render_to_response('index.html', {'success': False})


class RegisterForm(forms.Form):
    # email=forms.EmailField(max_length=50,label='邮箱',error_messages={'required':'请输入邮箱'})
    username = forms.CharField(max_length=50, label='用户名', error_messages={'required': '请输入用户名'})
    # pwd3 = forms.CharField(max_length=50, label='密码', error_messages={'required': '请输入密码'})
    password = forms.CharField(max_length=50, label='密码', error_messages={'required': '请再次输入密码'})


def register_page(request):  #
    if request.method == 'POST':  # 当提交表单时
        rf = RegisterForm(request.POST)  # rf 包含提交的数据
        if rf.is_valid():   # 如果提交的数据合法
            try:
                username = rf.cleaned_data['username']
                password = rf.cleaned_data['password']
                tmp = MyUser.objects.exclude(pk=request.user.pk)
                if tmp.filter(name=username).exists():  # 用户名判重
                    print "已注册1111"
                    return render_to_response('home.html', RequestContext(request, {'registered_name': True}))
                else:
                    MyUser.objects.create(name=username, password=password)
                    print "注册成功"
                    return HttpResponseRedirect('/main_page')
            except Exception, e:
                print e
                return render_to_response('errors.html', RequestContext(request, {'registered': True}))
        else:
            print "不合法填写"
            return  render_to_response('home.html')
    else:
        rf = RegisterForm()  # 当正常访问时
        return render_to_response('home.html', RequestContext(request, {'existed': False}))


def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/login')

def main_page(request):
    return render(request, 'home.html')

class GetId(forms.Form):
    number = forms.CharField(label='编号(0-1)')


def get_id(request):
    # if request.method=='POST':
    #     uid=GetId(request.POST)
    #     try:
    #         iv=uid.is_valid()
    #         num=uid.cleaned_data['number']
    db = Database()
    user_list = db.get_mysql_user(1, 20)
    dict_uid = dict()
    dict_uid['user_id'] = user_list
    post_data = json.dumps(dict_uid)
    pc = Page()
    pc.getId(post_data)
    return HttpResponse(post_data)
    #     except (),e:
    #         print e
    #
    # else :
    #     return render(request,'get_id.html')

def barchartData(request):
    data_dict={'a':1,'b':2,'c':3}
    y_axis=data_dict.keys()
    data=data_dict.values()
    return render_to_response('kaixin.html',{'y_axis':y_axis,'data':data})

def kaixin(request):
    data_dict={'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8}
    emos=['开心','快乐','满意','惊讶','不满','无奈','难过','痛恨']
    y_axis=data_dict.keys()
    datum=data_dict.values()
    return render_to_response('kaixin.html',{'y_axis':y_axis,'data':datum,'emos':emos})


def kuaile(request):
    string = u'Welcome to mysite!!'
    TutorialList = ["HTML", "CSS", "jQuery", "Python", "Django"]
    info_dict = {'label': u'键', 'content': u'值'}
    return render(request, 'kuaile.html', {'info_dict': info_dict})


def manyi(request):
    List = ['jian','zhi']
    Dict = {'a':'jian','b':'zhi'}
    keys=Dict.keys()
    values=Dict.values()
    return render(request, 'manyi.html',{
        'list':json.dumps(List),
        'keys':keys,'values':values
    })

def tonghen(request):
    List = ['自强学堂', '渲染Json到模板']
    Dict = {'site': '自强学堂', 'author': '涂伟忠'}
    return render(request, 'tonghen.html', {
            'List': json.dumps(List),
            'Dict': json.dumps(Dict)
        })

def jingya(request):
    return render(request, 'jingya.html')

def wunai(request):
    return render(request, 'wunai.html')

def nanguo(request):
    return render(request, 'nanguo.html')

def buman(request):
    return render(request, 'buman.html')
