from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, 'stock/home.html')

@login_required(login_url=('/accounts/login'))
def list_items(request):
    form = Stock.objects.all()
    return render(request, 'stock/list.html', {'form':form})

@login_required(login_url=('/accounts/login'))
def add_items(request):
    if request.method == 'POST':
        form = StockCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('stock:list')
    else:
        form = StockCreateForm()
    
    return render(request, 'stock/add.html', {'form': form})
