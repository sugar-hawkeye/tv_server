# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib import messages

from tv_server.settings.common import MEDIA_URL
from models import Video,Cover,VideoList,VideoCount

from forms import CoverForm,VideoListForm,VideoForm

# class VideoAboutAdmin(admin.ModelAdmin):
#     model = VideoAbout
#     raw_id_fields = ['video_id',]
#     filter_horizontal = ('about_video_id',)


class VideoCountAdmin(admin.TabularInline):
    model = VideoCount
    list_display = ('video_id', 'play_count', 'download_count','up_count','down_count')

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

class VideoListAdmin(admin.TabularInline):
    model = VideoList
    list_display = ('video_id', 'video_name', 'video_index','show_video','show_icon','is_publish')
    form = VideoListForm
    # search_fields = ('video_id','video_name')

    def show_icon(self,obj):
        if obj.video_icon:
            return u'<a href="%s%s"><img src="http://127.0.0.1:8000%s%s" height=60px></img></a>' % (MEDIA_URL,obj.show_icon,MEDIA_URL,obj.show_icon)
        else:
            return u'&nbsp;'
    show_icon.short_description = "图片"
    show_icon.allow_tags = True


class VideoAdmin(admin.ModelAdmin):
    fieldsets = (
        (None,{
            'fields':('video_name','video_desc','cover_pic','director','player','publish_time','downloadable','is_publish','is_serial')
        }),

        ('编辑标签', {
            # 'classes': ('collapse',),  # CSS
            'fields': ('channel_id', 'tag_id', 'tag_info'),
        })
    )
    form = VideoForm

    list_display = ('video_name','show_icon', 'channel_id', 'get_tag_id', 'is_publish', 'created_by')
    # radio_fields = {"channel_id": admin.HORIZONTAL}
    search_fields = ('video_name',)
    # filter_horizontal = ('tag_id','tag_info')
    inlines = [
        VideoCountAdmin,
        CoverAdmin,
        VideoListAdmin,

    ]

    def show_icon(self,obj):
        if obj.cover_pic:
            return u'<a href="%s%s"><img src="http://127.0.0.1:8000%s%s" height=60px></img></a>' % (MEDIA_URL,obj.cover_pic,MEDIA_URL,obj.cover_pic)
        else:
            return u'&nbsp;'
    show_icon.short_description = "封面"
    show_icon.allow_tags = True


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
# admin.site.register(VideoList,VideoListAdmin)
# admin.site.register(VideoAbout,VideoAboutAdmin)