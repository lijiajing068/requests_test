from django.contrib import admin
from sign.models import Event,Guest
# Register your models here.
class EventAdmin(admin.ModelAdmin):
    list_display = ['id','status','name','address','start_time']
    search_fields = ['name'] #搜索栏
    list_filter = ['status'] #过滤栏
class GuestAdmin(admin.ModelAdmin):
    list_display = ['realname','phone','email','sign','create_time','event']
admin.site.register(Event,EventAdmin)
admin.site.register(Guest,GuestAdmin)
