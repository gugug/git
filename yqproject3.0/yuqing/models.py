# coding=utf-8

from django.db import models
from django.contrib import admin


class Increment(models.Model):  # 事件描述表
    iid = models.IntegerField(auto_created=True, primary_key=True)
    event_id = models.CharField('事件id', max_length=20)
    check_time = models.DateTimeField('检测时间')
    comment_num = models.IntegerField('评论数', default=0)
    repost_num = models.IntegerField('转发数', default=0)
    like_num = models.IntegerField('点赞数', default=0)

    def __unicode__(self):
        return u'%s %s' % (self.event_id, self.check_time)

    class Meta:
        db_table = 'increment'


class IncrementAdimin(admin.ModelAdmin):
    list_display = ('event_id', 'check_time', 'comment_num', 'repost_num', 'like_num')
    list_filter = ('event_id', 'check_time')
    search_fields = ('event_id', 'check_time')


class NetworkScale(models.Model):  # 网络规模表(结果事件表)
    nid = models.IntegerField(auto_created=True, primary_key=True)
    event_id = models.CharField('事件id', max_length=20)
    check_time = models.DateTimeField('检测时间')
    corpus_dir = models.CharField('语料文本', max_length=300)
    label_dir = models.CharField(max_length=300)
    leader = models.CharField('核心人物', max_length=50)

    def __unicode__(self):
        return u'%s %s' % (self.event_id, self.check_time)

    class Meta:
        db_table = 'networkscale'


class NetworkScaleAdmin(admin.ModelAdmin):
    list_display = ('event_id', 'check_time', 'corpus_dir', 'label_dir', 'leader')
    list_filter = ('event_id', 'check_time', 'corpus_dir',  'label_dir', 'leader')
    search_fields = ('event_id', 'check_time', 'corpus_dir', 'label_dir', 'leader')


class Event(models.Model):  # 事件表
    event_id = models.CharField('事件id', max_length=20, primary_key=True)
    post_time = models.DateTimeField('发起时间')
    topic = models.CharField('事件主题', max_length=100)
    topic_words = models.CharField('主题词', max_length=300)
    origin = models.CharField('传播源', max_length=100)
    link = models.CharField('新闻链接', max_length=100)

    def __unicode__(self):
        return u'%s %s %s' % (self.event_id, self.post_time, self.topic)

    class Meta:
        db_table = 'event'


class EventAdmin(admin.ModelAdmin):
    search_fields = ('event_id', 'post_time', 'topic', 'topic_words', 'origin', 'link', 'content')


class Headhunter(models.Model):  # 猎头信息表
    user_id = models.CharField('用户id', max_length=20, primary_key=True)
    user_name = models.CharField('昵称', max_length=20)
    gender = models.CharField('性别', max_length=6, default='未知')
    birth = models.DateField('生日')
    vip_state = models.CharField('认证信息', max_length=30, default='非认证用户')
    location = models.CharField('地区', max_length=10)
    profile = models.TextField('简介', max_length=300)
    tag = models.CharField('标签', max_length=200, default='无')
    fans_num = models.IntegerField('粉丝数', default=0)
    follow_num = models.IntegerField('关注数', default=0)
    blog_num = models.IntegerField('微博数', default=0)

    def __unicode__(self):
        return u'%s %s %s' % (self.user_name, self.vip_state, self.location)

    class Meta:
        db_table = 'headhunter'


class HeadhunterAdmin(admin.ModelAdmin):
    search_fields = ('user_id', 'user_name', 'vip_state', 'location')


class Participate(models.Model):  # 用户事件关系表
    user_id = models.CharField('用户id', max_length=20)
    event_id = models.CharField('事件id', max_length=20)

    class Meta:
        db_table = 'participate'
        unique_together = ('user_id', 'event_id')


class ParticipateAdmin(admin.ModelAdmin):
    search_fields = ('user_id', 'event_id')


class Content(models.Model):
    blog_id = models.CharField('博文id', max_length=20, primary_key=True)
    post_time = models.DateTimeField('博文发表时间',null=True)
    event_id = models.CharField('事件id', max_length=20)
    content = models.TextField('事件内容')
    keywords = models.TextField('事件关键词',null=True)

    class Meta:
        db_table = 'content'


class ContentAdmin(admin.ModelAdmin):
    search_fields = ('event_id',)
