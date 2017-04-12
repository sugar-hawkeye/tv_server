# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib import messages

from tv_server.settings.common import MEDIA_URL
from models import Video,Cover,VideoList

from forms import CoverForm,VideoListForm

class CoverAdmin(admin.TabularInline):
    model = Cover
    form = CoverForm
    list_display = ('video_id','image_type','show_icon')

    # def save_model(self, request, obj, form, change):
    #     if not request.FILES:
    #         messages.error(request, ' 图片不能为空')
    #         obj.cover_pic = None
    #
    #     else:
    #         obj.created_by = request.user
    #         super(CoverAdmin, self).save_model(request, obj, form, change)




    def show_icon(self,obj):
        if obj.cover_pic:
            return u'<a href="%s%s"><img src="http://127.0.0.1:8000%s%s" height=60px></img></a>' % (MEDIA_URL,obj.cover_pic,MEDIA_URL,obj.cover_pic)
        else:
            return u'&nbsp;'
    show_icon.short_description = "封面"
    show_icon.allow_tags = True

class VideoListAdmin(admin.ModelAdmin):
    # model = VideoList
    list_display = ('video_id', 'video_name', 'video_index','show_video','video_icon','is_publish')
    form = VideoListForm
    # search_fields = ('video_id','video_name')

    def show_video(self,obj):
        if obj.video_url:
            return u'<a href="%s%s"><video src="http://127.0.0.1:8000%s%s" height=60px></video></a>' % (MEDIA_URL,obj.video_url,MEDIA_URL,obj.video_url)
        else:
            return u'&nbsp;'
    show_video.short_description = "视频"
    show_video.allow_tags = True


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





admin.site.register(Video,VideoAdmin)
admin.site.register(VideoList,VideoListAdmin)
# admin.site.register(Cover,CoverAdmin)