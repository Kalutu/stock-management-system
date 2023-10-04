from django.shortcuts import render
from .forms import *

# Create your views here.
def list_items(request):
    form = Stock.objects.all()
    return render(request, 'stock/list.html', {'form':form})