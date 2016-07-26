# coding=utf-8

from django import forms
from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from yuqing.jsondump import *
from yuqing.main_run import *
from crawler.class_event import *
from crawler.class_content import *
from crawler.class_headhunter import *


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


def network(request, event_id, ctime):
    # if request.method == 'POST':
    #     event_id = request.POST['event_id']
    #     ctime = request.POST['ctime']
    hh= Headhunter()
    event = Event().get_topic(event_id)  # topic
    result = dump_force(event_id, ctime)
    scale = result[2]
    node_data = result[0]
    edge_data = result[1]
    leader = result[3]
    info_list = []
    pic_dir = result[4]
    for i in leader:
        info = hh.get_info(i) #{}
        info_list.append(info)
    return render(request, 'network.html', {'scale': scale, 'node_data': node_data, 'edge_data': edge_data,
                                            'event': event['etopic'], 'leader': leader, 'info': info_list,
                                            'pic_dir': pic_dir})

    # else:
    #     return HttpResponseRedirect('/linechart/')


def line_chart(request, topic=''):
    eid_tuple = ()
    if request.method == 'POST':
        sf = SearchForm(request.POST)
        if sf.is_valid():
            search_words = sf.cleaned_data['input_words']
            eid_tuple = Event().search_vague_topic(search_words)  # ({eid,etp},{})

        else:
            print 'invalid form'
    else :
        eid_tuple = Event().search_exact_topic(topic)
        # print topic
        # print eid_tuple

    if len(eid_tuple) == 0:
        return render_to_response('error.html')

    if len(eid_tuple) > 1:
        event_list = []
        for i in eid_tuple:
            event_list.append(i)
        return render(request, 'list.html', {'event_list': event_list})

    else:
        event_id = eid_tuple[0]['event_id']
        inc = Increment()
        rows = inc.get_data(event_id)
        event = Event().get_topic(event_id)
        topic_words = Content().get_keywords(event_id)
        cmt = inc.get_comment(event_id)
        rpt = inc.get_repost(event_id)
        lik = inc.get_like(event_id)
        cnt = Content().get_content(event_id)
        print 'eve', event_id, event
        xaxis = str(inc.time_list)
        yaxis = str(inc.scale_rate)
        seris_data = str(inc.scale_rate)
        if len(rows) == 0:
            default = True

        else:
            default = False
            old_file = open(BASE_DIR + '/static/scripts/lineChart.js', 'rw')
            new_file = open(BASE_DIR + '/static/scripts/line_chart.js', 'w+')
            rw = old_file.readlines()
            oldx = "['6:00','7:00','8:00','9:00','10:00','11:00','12:00','13:00','14:00','15:00','16:00','17:00','18:00','19:00','20:00','21:00','22:00','23:00','24:00','1:00','2:00','3:00','4:00']"
            oldd = "[1,3,5,10,12,18,28,30,20,15,12,9,7,8,12,19,16,10,7,4,2,0,0,0,0,0]"
            rw[41] = rw[41].replace(oldx, xaxis)
            rw[74] = rw[74].replace(oldd, seris_data)
            # print rw[42]
            # print rw[75]
            for i in rw:
                new_file.write(i)
        return render(request, 'lineChart.html',
                      {'default': default, 'event_id':event_id, 'event': event['etopic'], 'topic_words': topic_words['keywords'],
                       'cmt': cmt['comment_num'], 'rpt': rpt['repost_num'], 'lik': lik['like_num'],
                       'cnt': cnt['content']})
