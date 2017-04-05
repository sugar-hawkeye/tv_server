# -*- coding: utf-8 -*-


from django.contrib import admin

from models import Video,Cover,VideoList

class CoverAdmin(admin.StackedInline):
    model = Cover
    list_display = ('video_id', 'image_type', 'cover_pic',)

class VideoListAdmin(admin.StackedInline):
    model = VideoList
    list_display = ('video_id', 'video_name', 'video_index','player_url','icon','is_publish')


class VideoAdmin(admin.ModelAdmin):
    list_display = ('video_name', 'channel_id','get_tag_id','get_tag_info','is_publish', 'created_by')
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
        return ([str(p) for p in obj.tag_id.all()])
    get_tag_id.short_description = "分类标签"

    def get_tag_info(self,obj):
        return ([str(p) for p in obj.tag_info.all()])
    get_tag_info.short_description = "标签详情"

admin.site.register(Video,VideoAdmin)