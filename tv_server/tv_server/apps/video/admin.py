# -*- coding: utf-8 -*-
from django.contrib import admin
from tv_server.settings.common import MEDIA_URL
from models import Video,Cover,VideoList

from forms import CoverForm

class CoverAdmin(admin.TabularInline):
    form = CoverForm

    model = Cover

class VideoListAdmin(admin.TabularInline):
    model = VideoList
    list_display = ('video_id', 'video_name', 'video_index','player_url','icon','is_publish')
    # search_fields = ('video_id','video_name')

    #
    # def save_model(self, request, obj, form, change):
    #     obj.created_by = request.user
    #     super(VideoListAdmin, self).save_model(request, obj, form, change)





class VideoAdmin(admin.ModelAdmin):
    fieldsets = (
        (None,{
            'fields':('video_name','video_desc','director','player','publish_time','downloadable','is_publish','is_serial')
        }),

        ('编辑标签', {
            'classes': ('collapse',),  # CSS
            'fields': ('channel_id', 'tag_id', 'tag_info'),
        })
    )

    list_display = ('video_name', 'channel_id', 'get_tag_id', 'is_publish', 'created_by')

    search_fields = ('video_name',)
    filter_horizontal = ('tag_id','tag_info')
    inlines = [
        CoverAdmin,
        VideoListAdmin,
    ]



    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        super(VideoAdmin,self).save_model(request,obj,form,change)

    def get_tag_id(self,obj):
        names = [str(p) for p in obj.tag_info.all()]
        title = ''
        for name in names:
            title += name[name.find('--') + 2:] + ","
        return title
    get_tag_id.short_description = "标签"



    # def get_tag_info(self,obj):
    #     names = [str(p) for p in obj.tag_info.all()]
    #     title = ''
    #     for name in names:
    #         title += name[name.find('---') + 3:]+","
    #     return title
    #
    # get_tag_info.short_description = "二级标签"

admin.site.register(Video,VideoAdmin)
# admin.site.register(VideoList,VideoListAdmin)