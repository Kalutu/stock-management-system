from django.urls import path
from .views import *

urlpatterns = [
    path('list/', list_items, name='list'),
]
