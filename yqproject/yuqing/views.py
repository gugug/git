# coding=utf-8

from django import forms
from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from yuqing.jsondump import *
from yqproject.settings import *
from yuqing.main_run import *
from crawler.class_event import *

# Create your views here.


def ajax_list(request):
    a = range(100)
    return JsonResponse(a, safe=False)


def ajax_dict(request):
    name_dict = {'twz': 'Love python and Django', 'zqxt': 'I am teaching Django'}
    return JsonResponse(name_dict)


def homepage(request):
    data = dump_time_line()
    # print data
    # data = [{'topic':u'烧鸡公双方了时间','month':4L,'day':30L},{'topic':u'222','month':4L,'day':15L},{'topic':u'111','month':4,'day':1}]
    # data = [{'a':'aaa'},{'b':'bbb'}]
    return render_to_response('index.html', {'data': data})

class SearchForm(forms.Form):
    input_words = forms.CharField(max_length=100)

def network(request):
    if request.method == 'POST':
        file = request.POST['file']
        print file

    event_id='topicM_DtGq72V9U'
    event = Event().get_topic_by_id(event_id)

    node_data = dump_force()[0]
    edge_data = dump_force()[1]
    return render(request, 'network.html', {'node_data': node_data, 'edge_data': edge_data,'event':event['topic']})

def line_chart(request):
    event_id =''
    if request.method == 'POST':
        sf = SearchForm(request.POST)
        print 'bbb',request.POST
        if sf.is_valid():
            search_words = sf.cleaned_data['input_words']
            event_id = Event().search_topic(search_words)

        else:
            print 'invalid form'

    if event_id == '000':
        return render_to_response('error.html')

    else:
        inc = Increment()
        rows = inc.get_data(event_id)
        event = Event().get_topic_by_id(event_id)
        topic_words = Content().get_topic_words(event_id)
        # print topic_words
        cmt = inc.get_comment(event_id)
        rpt = inc.get_repost(event_id)
        lik = inc.get_like(event_id)
        cnt = Content().get_main_content(event_id)
        print 'eve', event_id, event
        xaxis = str(inc.time_list)
        yaxis = str(inc.scale_rate)
        seris_data = str(inc.scale_rate)
        if len(rows) ==0:
            # return HttpResponseRedirect('/linechart/')
            return render(request,'lineChart.html',{'default':True,'event':event['topic'],'topic_words':topic_words['keywords'],
                                                    'cmt':cmt['comment_num'],'rpt':rpt['repost_num'],'lik':lik['like_num'],'cnt':cnt['content']})
        old_file = open(BASE_DIR + '/static/scripts/lineChart.js', 'rw')
        new_file = open(BASE_DIR + '/static/scripts/line_chart.js', 'w+')
        a = old_file.readlines()
        a[40] = a[40].replace('xaxis', xaxis)
        a[71] = a[71].replace('seris_data', seris_data)
        for i in a:
            new_file.write(i)
        return render(request, 'lineChart.html',{'default':False})
