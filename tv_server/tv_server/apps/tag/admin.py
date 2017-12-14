from django.contrib import admin

from models import Tag,TagInfo
from .forms import TagForm

class TagAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'channel_id', 'priority', 'is_publish','created_by')
    # raw_id_fields = ('channel_id',)
    # radio_fields = {"channel_id": admin.HORIZONTAL}
    form = TagForm

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        super(TagAdmin, self).save_model(request, obj, form, change)




class TagInfoAdmin(admin.ModelAdmin):
    list_display = ('id','title','tag_id','channel_id', 'priority', 'is_publish','created_by')
    # radio_fields = {"tag_id": admin.HORIZONTAL}


    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        super(TagInfoAdmin, self).save_model(request, obj, form, change)

admin.site.register(Tag, TagAdmin)
admin.site.register(TagInfo, TagInfoAdmin)