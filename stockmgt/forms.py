from django import forms
from .models import *

class StockCreateForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['category', 'item_name', 'quantity']
        
    def clean_item_name(self):
          item_name = self.cleaned_data.get('item_name')
          if not item_name:
            raise forms.ValidationError("This field is required")
          for instance in Stock.objects.all():
              if instance.item_name == item_name:
                raise forms.ValidationError(str(item_name) + ' is already created')
          return item_name
        
    def clean_category(self):
          category = self.cleaned_data.get('category')
          if not category:
            raise forms.ValidationError("This field is required")
          return category

class StockSearchForm(forms.ModelForm):
   class Meta:
     model = Stock
     fields = ['category', 'item_name', 'export_to_CSV']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']