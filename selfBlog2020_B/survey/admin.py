from django.contrib import admin

from . import models

admin.site.register(models.ClassList)
admin.site.register(models.Questionnaire)
admin.site.register(models.Questions)
admin.site.register(models.Option)
admin.site.register(models.Answer)
admin.site.register(models.UserProfile)
admin.site.register(models.Image)
