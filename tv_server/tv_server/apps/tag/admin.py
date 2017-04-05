from django.contrib import admin

from models import Tag,TagInfo


class TagAdmin(admin.ModelAdmin):
    list_display = ('title', 'channel_id', 'priority', 'is_publish','created_by')
    raw_id_fields = ('channel_id',)

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        super(TagAdmin, self).save_model(request, obj, form, change)


class TagInfoAdmin(admin.ModelAdmin):
    list_display = ('tag_id', 'title', 'priority', 'is_publish','created_by')
    raw_id_fields = ('tag_id',)

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        super(TagInfoAdmin, self).save_model(request, obj, form, change)

admin.site.register(Tag, TagAdmin)
admin.site.register(TagInfo, TagInfoAdmin)