from django.contrib import admin
from dua.models import *
# Register your models here.

admin.site.register(WeiboText,WeiboAdmin)
admin.site.register(GDFan,FansAdimin)
admin.site.register(GDFollow,FollowsAdimin)
admin.site.register(SinaUser,SinaUserAdimin)
admin.site.register(MyUser,MyUsersAdimin)