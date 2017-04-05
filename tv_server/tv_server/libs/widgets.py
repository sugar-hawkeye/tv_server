from django.forms import FileInput,Widget,ClearableFileInput
from django.utils.safestring import mark_safe
from django.template.loader import render_to_string

from tv_server.settings.common import BASE_DIR

class SingleImageInput(ClearableFileInput):
    template_name = BASE_DIR+'/templates/admin/single_image_upload.html'



    def render(self, name, value, attrs=None):
        if name == 'icon' and value:
            return mark_safe(render_to_string(self.template_name,context={'icon':'http://127.0.0.1:8000'+value.url}))
        else:
            return mark_safe(render_to_string(self.template_name,))

    class Media:
        css = {
            'all': ('css/single_image_upload.css',)
        }
        js = ('js/single_image_upload.js',)
