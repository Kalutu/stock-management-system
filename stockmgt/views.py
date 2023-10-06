from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse
import csv

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
                    category__name__icontains=form['category'].value(),
                    item_name__icontains=form['item_name'].value()
                )
            
            context={
                    'queryset':queryset,
                    'form':form
            }

            if form['export_to_CSV'].value() == True:
                response = HttpResponse(content_type='text/csv')
                response['Content-Disposition'] = 'attachment; filename="Stocklist.csv"'
                writer = csv.writer(response)
                writer.writerow(['CATEGORY', 'ITEM NAME', 'QUANTITY'])
                instance = queryset
                for stock in instance:
                    writer.writerow([stock.category, stock.item_name, stock.quantity])
                return response
       
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

@login_required(login_url=('/accounts/login'))
def update_item(request, id):
    queryset = Stock.objects.get(id=id)
    form = StockCreateForm(instance=queryset)

    if request.method == 'POST':
        form = StockUpdateForm(request.POST,instance=queryset)
        if form.is_valid:
            form.save()
            messages.success(request, "Updated Successfully")
            return redirect('stock:list')

    context = {
        'form':form
    }  
    return render(request, 'stock/add.html', context)

@login_required(login_url=('/accounts/login'))
def delete_item(request, id):
    queryset = Stock.objects.get(id=id)
    if request.method=='POST':
        queryset.delete()
        messages.success(request, "Deleted Successfully")
        return redirect('stock:list')
    return render(request, 'stock/delete.html')

@login_required(login_url=('/accounts/login'))
def add_category(request):
    form = CategoryForm()
    context={
        'form':form
    }
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Category added Successfully")
            return redirect('stock:add')
    return render(request, 'stock/category.html', context)

@login_required(login_url=('/accounts/login'))
def stock_detail(request, id):
    queryset = Stock.objects.get(id=id)
    context={
        'queryset': queryset,
    }
    return render(request, 'stock/detail.html', context)

@login_required(login_url=('/accounts/login'))
def issue_item(request, id):
    instance = Stock.objects.get(id=id)
    form = IssueForm()
    context = {
        'queryset': instance,
        'form': form
    }
    
    if request.method == 'POST':
        form = IssueForm(request.POST)
        if form.is_valid():
            try:
                issue_quantity = int(form.cleaned_data['issue_quantity'])
                instance.quantity -= issue_quantity
                instance.save()
                return redirect('/stock/detail/' + str(instance.id))
            except ValueError:
                pass
    return render(request, "stock/add.html", context)




@login_required(login_url=('/accounts/login'))
def receive_item(request, id):
    instance = Stock.objects.get(id=id)
    form = ReceiveForm()
    context = {
        'queryset': instance,
        'form': form
    }
    
    if request.method == 'POST':
        form = ReceiveForm(request.POST)
        if form.is_valid():
            try:
                receive_quantity = int(form.cleaned_data['receive_quantity'])
                instance.quantity += receive_quantity
                instance.save()
                return redirect('/stock/detail/' + str(instance.id))
            except ValueError:
                pass
    return render(request, "stock/add.html", context)

@login_required(login_url=('/accounts/login'))
def reorder_level(request, id):
    queryset = Stock.objects.get(id=id)
    form = ReorderLevelForm(request.POST or None, instance=queryset)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Reorder level for " + str(instance.item_name) + " is updated to " + str(instance.reorder_level))
        return redirect("stock:list")
    context = {
			"instance": queryset,
			"form": form,
		}
    return render(request, "stock/add.html", context)

@login_required(login_url=('/accounts/login'))
def history(request):
    queryset = StockHistory.objects.all()
    context = {
		"queryset": queryset,
	}
    return render(request, "stock/history.html",context)