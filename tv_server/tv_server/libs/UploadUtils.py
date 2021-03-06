import datetime
from django.contrib.auth.hashers import  PBKDF2PasswordHasher

def channel_path(instance,filename):
    name = datetime.datetime.now().strftime("%Y-%m-%d %H:%I:%S")
    return 'cover/channel/%s' % instance.id+name+filename;

def video_path(instance,filename):
    name = datetime.datetime.now().strftime("%Y-%m-%d %H:%I:%S")
    return 'cover/video/%s' % instance.id+name+filename;

def avator_path(instance,filename):
    name = datetime.datetime.now().strftime("%Y-%m-%d %H:%I:%S")
    return 'manager/avator/%s' % name+filename