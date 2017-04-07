# -*- coding: utf-8 -*-

from django.contrib import admin
from django.contrib.admin import AdminSite
from tv_server.settings.common import MEDIA_URL


from models import Channel
from forms import ChannelForm


class ChannelAdmin(admin.ModelAdmin):
    fields = ('title', 'cover', 'priority','is_publish')
    list_display = ('title','show_icon','created_by','created_at','is_publish')

    form = ChannelForm


    readonly_fields = ('show_icon',)


    def save_model(self, request, obj, form, change):
        if not request.FILES:
            obj.cover = None
        obj.created_by = request.user

        super(ChannelAdmin,self).save_model(request,obj,form,change)



    def show_icon(self,obj):
        if obj.cover:
            return u'<a href="%s%s"><img src="http://127.0.0.1:8000%s%s" height=60px/></a>' % (MEDIA_URL,obj.cover,MEDIA_URL,obj.cover)
        else:
            return u'&nbsp;'
    show_icon.short_description = "Cover"
    show_icon.allow_tags = True

admin.AdminSite.site_header = '视频管理系统'
admin.AdminSite.site_title = '视频管理系统'
admin.site.register(Channel, ChannelAdmin)