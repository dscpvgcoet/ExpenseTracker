# -*- coding: utf-8 -*-
"""
    Currency administration
"""
from django.contrib import admin
from django_723e.models.currency.models import Currency

class CurrencyAdmin(admin.ModelAdmin):
    """
        Administrate Currency model
    """
    list_display = ('name', 'sign', 'space', 'after_amount',)

admin.site.register(Currency, CurrencyAdmin)
