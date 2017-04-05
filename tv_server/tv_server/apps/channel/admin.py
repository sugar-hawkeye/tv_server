# -*- coding: utf-8 -*-

from django.contrib import admin
from django.contrib.admin import AdminSite
from tv_server.settings.common import MEDIA_URL


from models import Channel
from forms import ChannelForm


class ChannelAdmin(admin.ModelAdmin):
    fields = ('title', 'icon', 'priority','is_publish')
    list_display = ('title','show_icon','created_by','created_at','is_publish')

    form = ChannelForm


    readonly_fields = ('show_icon',)


    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        super(ChannelAdmin,self).save_model(request,obj,form,change)

    def get_form(self, request, obj=None, **kwargs):
        return super(ChannelAdmin, self).get_form(request, obj, **kwargs)

    def get_urls(self):
        return super(ChannelAdmin,self).get_urls()

    def change_view(self, request, object_id, form_url='', extra_context=None):

        return super(ChannelAdmin,self).change_view(request,object_id,form_url,extra_context)

    def show_icon(self,obj):
        if obj.icon:
            return u'<a href="%s%s"><img src="http://127.0.0.1:8000%s%s" height=60px/></a>' % (MEDIA_URL,obj.icon,MEDIA_URL,obj.icon)
        else:
            return u'&nbsp;'
    show_icon.short_description = "Icon"
    show_icon.allow_tags = True

admin.AdminSite.site_header = '视频管理系统'
admin.AdminSite.site_title = '视频管理系统'
admin.site.register(Channel, ChannelAdmin)