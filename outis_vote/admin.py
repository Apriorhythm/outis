# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import OutisPostVote, OutisCommentVote


# Register your models here.

admin.site.register(OutisPostVote)
admin.site.register(OutisCommentVote)
