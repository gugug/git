#coding=utf-8
from django.db import models,connection
from django.contrib import admin
class WbManager(models.Manager):
    def id_a(self, id):
        cursor = connection.cursor()  #三个双引号表示可以换行,distinct 可以去重
        cursor.execute("""
            SELECT DISTINCT weibo
            FROM dua_dbtest2
            WHERE id = %s""", [id])
        return [row[0] for row in cursor.fetchone()]

class WeiboText(models.Model):
    user_id=models.CharField(max_length=20)
    weibo=models.TextField()
    time=models.CharField(max_length=30)
    # objects=WbManager
    def __unicode__(self):
        return u'%s %s' %(self.user_id,self.time)
    class Meta:
        db_table='weibotext'


class WeiboAdmin(admin.ModelAdmin):
    list_display = ('user_id','time','weibo')
    search_fields = ('user_id','time')

class GDFan(models.Model):
    user_id=models.CharField(max_length=20)
    gdfans_id=models.CharField(max_length=20)
    def __unicode__(self):
        return u'%s %s' %(self.user_id,self.gdfans_id)
    class Meta:
        db_table='gdfan'
        unique_together=('user_id','gdfans_id')



class FansAdimin(admin.ModelAdmin):
    list_display = ('user_id','gdfans_id')
    list_filter =('user_id',)
    search_fields = ('user_id','gdfans_id',)

class GDFollow(models.Model):
    user_id=models.CharField(max_length=20)
    gdfollows_id=models.CharField(max_length=20)
    def __unicode__(self):
        return u'%s %s' %(self.user_id,self.gdfollows_id)
    class Meta:
        db_table='gdfollow'
        unique_together=('user_id','gdfollows_id')


class FollowsAdimin(admin.ModelAdmin):
    list_display = ('user_id','gdfollows_id')
    list_filter = ('user_id',)
    search_fields = ('user_id','gdfollows_id',)

class SinaUser(models.Model):
    user_id=models.CharField(max_length=20)
    user_name=models.CharField(max_length=100,null=True)
    def __unicode__(self):
        return self.user_id
    class Meta:
        db_table='sinauser'
        unique_together=('user_id','user_name')
        unique_together = (('user_id','user_name'),)

class MyUser(models.Model):
    name=models.CharField(max_length=100)
    password=models.CharField(max_length=50)
    # email=models.EmailField(max_length=50)
    def __unicode__(self):
        return self.name
    class Meta:
        db_table='myuser'




class MyUsersAdimin(admin.ModelAdmin):
    list_display = ('name',)


class SinaUserAdimin(admin.ModelAdmin):
    list_display = ('user_id','user_name')
    search_fields = ('user_id','user_name')

