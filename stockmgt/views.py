from django.shortcuts import render, redirect
from .forms import *

# Create your views here.
def home(request):
    return render(request, 'stock/home.html')

def list_items(request):
    form = Stock.objects.all()
    return render(request, 'stock/list.html', {'form':form})

def add_items(request):
    if request.method == 'POST':
        form = StockCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('stock:list')
    else:
        form = StockCreateForm()
    
    return render(request, 'stock/add.html', {'form': form})
