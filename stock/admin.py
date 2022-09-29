
from stock.models import Option, Stock
from django.contrib import admin




class StockAdmin(admin.ModelAdmin):
    list_display = [ 'num_in_stock','low_stock_threshold', 'product' ]
    fieldsets = (
        (None, {
            'fields': ( 'num_in_stock','low_stock_threshold', 'product', 'option')
        }),
    )
admin.site.register(Stock, StockAdmin)


class OptionAdmin(admin.ModelAdmin):
   
    list_display = ['name', 'type', 'value', 'required']
    fieldsets = (
        (None, {
            'fields': ('name', 'type', 'value', 'required')
        }),
    )
admin.site.register(Option, OptionAdmin)


