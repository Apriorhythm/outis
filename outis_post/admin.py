# -*- coding: utf-8 -*-
from django.contrib import admin
from django.db import models


from .models import OutisCategory, OutisPost

admin.site.register(OutisCategory)
admin.site.register(OutisPost)


