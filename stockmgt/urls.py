from django.urls import path
from .views import *

app_name = 'stock'

urlpatterns = [
    path('list/', list_items, name='list'),
    path('add/', add_items, name='add'),
    path('add_category/', add_category, name='add_category'),
    path('update/<str:id>/', update_item, name='update'),
    path('delete/<str:id>/', delete_item, name='delete'),
    path('detail/<str:id>/', stock_detail, name="detail"),
    path('issue/<str:id>/', issue_item, name="issue"),
    path('receive/<str:id>/', receive_item, name="receive"),
    path('reorder/<str:id>/', reorder_level, name="reorder"),
    path('history/', history, name='history'),
]
