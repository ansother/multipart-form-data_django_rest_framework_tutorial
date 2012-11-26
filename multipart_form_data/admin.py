#!/usr/bin/env python
# encoding: utf-8
"""
admin.py
"""

from multipart_form_data.models import Files
from django.contrib import admin

class FilesAdmin(admin.ModelAdmin):
    list_display = ('created', 'docfile')

admin.site.register(Files, FilesAdmin)
