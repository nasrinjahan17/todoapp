from django.contrib import admin
from .models import *
# Register your models here.
class To_DoAdmin(admin.ModelAdmin):
    list_display = ['user','title']

admin.site.register(To_Do,To_DoAdmin)

