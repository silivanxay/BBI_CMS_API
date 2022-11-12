
from stock.models import Stock
from django.contrib import admin

class StockAdmin(admin.ModelAdmin):
    list_display = [ 'num_in_stock','low_stock_threshold', 'product']
    fieldsets = (
        (None, {
            'fields': ( 'num_in_stock','low_stock_threshold', 'product')
        }),
    )
    # def save_model(self, request, obj, form, change):
    #     obj.product_id = request.product.id
    #     super().save_model(request, obj, form, change)
admin.site.register(Stock, StockAdmin)



