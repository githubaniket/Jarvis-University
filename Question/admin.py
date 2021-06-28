from django.contrib import admin

from . import models

admin.site.register(models.StudentQuestion)
admin.site.register(models.Answers)
