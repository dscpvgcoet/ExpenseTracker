"""
    Admin code for categories module
"""

from django.contrib import admin
from django_723e.models.categories.models import Category

class CategoryAdmin(admin.ModelAdmin):
    """
        Deliver category model
    """
    list_display = ('user', 'name', 'description', 'color', 'icon', 'parent', 'active')

admin.site.register(Category, CategoryAdmin)
