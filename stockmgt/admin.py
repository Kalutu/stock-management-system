from django.contrib import admin
from .models import Stock
from .forms import StockCreateForm

# Register your models here.
class StockCreateAdmin(admin.ModelAdmin):
   form = StockCreateForm
   list_display = ['category', 'item_name', 'quantity']
   list_filter = ['category']
   search_fields = ['category', 'item_name']


admin.site.register(Stock, StockCreateAdmin)
