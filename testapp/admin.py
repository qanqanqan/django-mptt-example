from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from .models import Category, Node


admin.site.register(Category, MPTTModelAdmin)
admin.site.register(Node)
