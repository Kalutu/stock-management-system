from django.urls import path
from .views import *

app_name = 'stock'

urlpatterns = [
    path('list/', list_items, name='list'),
    path('add/', add_items, name='add'),
]
