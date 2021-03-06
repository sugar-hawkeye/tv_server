from django.forms import FileInput,Widget,ClearableFileInput
from django.utils.safestring import mark_safe
from django.template.loader import render_to_string
from tv_server.settings.common import BASE_DIR

from tv_server.settings.common import MEDIA_URL

class SingleImageInput(ClearableFileInput):
    template_name = BASE_DIR+'/templates/admin/single_image_upload.html'



    def render(self, name, value, attrs=None):

        namestr = str(name).replace('-', '_')
        idstr = attrs['id'].replace('-', '_')
        context = {'id_key': idstr, 'name': name,
                   'method':  namestr + idstr + '()'}

        if value :
            context['file'] = 'http://127.0.0.1:8000' + MEDIA_URL+value.name
            # context.setdefault('icon',default=('http://127.0.0.1:8000' + value.url))
        return mark_safe(render_to_string(self.template_name, context=context))

    class Media:
        css = {
            'all': ('css/single_image_upload.css',)
        }

