from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Blog)
admin.site.register(models.Passage)
admin.site.register(models.Tag)
admin.site.register(models.Img)
admin.site.register(models.Recording)
admin.site.register(models.LeaveMessage)
admin.site.register(models.Music)
admin.site.register(models.Cartoon)
admin.site.register(models.Video)
admin.site.register(models.ReplyMessage)