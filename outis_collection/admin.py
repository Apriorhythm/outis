# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import OutisPostCollection, OutisUserCollection


admin.site.register(OutisPostCollection)
admin.site.register(OutisUserCollection)

