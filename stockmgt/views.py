from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, 'stock/home.html')

@login_required(login_url=('/accounts/login'))
def list_items(request):
    queryset = Stock.objects.all()
    form = StockSearchForm()
    context={
        'queryset':queryset,
        'form':form
    }
    if request.method == 'POST':
        form = StockSearchForm(request.POST)
        if form.is_valid():
            queryset = Stock.objects.filter(
                category__icontains=form['category'].value(),
                item_name__icontains=form['item_name'].value()
				)
            context={
                    'queryset':queryset,
                    'form':form
            }
            
    return render(request, 'stock/list.html', context)

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
