# -*- coding: utf-8 -*-
from django.contrib import admin
from django.db import models
#from django import forms

# Register your models here.


from .models import OutisCategory, OutisPost, OutisComment


#class OutisCategoryAdmin(admin.AdminModel):
#    list_display = ('name')


admin.site.register(OutisCategory)
admin.site.register(OutisPost)
admin.site.register(OutisComment)


