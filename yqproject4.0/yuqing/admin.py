from django.contrib import admin

# Register your models here.

from yuqing.models import *

admin.site.register(Event,EventAdmin)
admin.site.register(NetworkScale,NetworkScaleAdmin)
admin.site.register(Increment,IncrementAdimin)
admin.site.register(Headhunter,HeadhunterAdmin)
admin.site.register(Content,ContentAdmin)
admin.site.register(Participate,ParticipateAdmin)