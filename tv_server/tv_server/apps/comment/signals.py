import django.dispatch

custom_post_save = django.dispatch.Signal(providing_args=["ancestor","descendant"])

def save_handler(sender, **kwargs):
    print('save_handler')