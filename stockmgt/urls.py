from django.urls import path
from .views import *

app_name = 'stock'

urlpatterns = [
    path('list/', list_items, name='list'),
    path('add/', add_items, name='add'),
    path('update/<int:id>/', update_item, name='update'),
    path('delete/<int:id>/', delete_item, name='delete'),
]
