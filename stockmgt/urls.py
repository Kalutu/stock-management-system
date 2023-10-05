from django.urls import path
from .views import *

app_name = 'stock'

urlpatterns = [
    path('list/', list_items, name='list'),
    path('add/', add_items, name='add'),
    path('add_category/', add_category, name='add_category'),
    path('update/<int:id>/', update_item, name='update'),
    path('delete/<int:id>/', delete_item, name='delete'),
]
