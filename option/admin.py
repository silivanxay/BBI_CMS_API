from option.models import Option
from django.contrib import admin


class OptionAdmin(admin.ModelAdmin):
   
    list_display = ['name', 'type', 'value', 'required', 'stock']
    fieldsets = (
        (None, {
            'fields': ('name', 'type', 'value', 'required', 'stock')
        }),
    )
admin.site.register(Option, OptionAdmin)