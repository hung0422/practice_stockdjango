from django.shortcuts import render, redirect
from .models import Twii, PredictionRecord, PredictionCategory
from .forms import RecordForm, CategoryForm
from django.db.models import Sum

# Create your views here.
def menu(request):
    return render(request, 'prediction/menu.html', locals())

def predict(request):
    alllist = Twii.objects.filter().order_by('-date')[:10]
    return render(request, 'prediction/predict.html', locals())

def detail(request, date):
    list = Twii.objects.get(date=date)
    return render(request, 'prediction/detail.html', locals())

def bookkeeping(request):
    income = PredictionRecord.objects.filter(balance_type='收入').aggregate(Sum('cash'))
    income = income['cash__sum']
    outcome = PredictionRecord.objects.filter(balance_type='支出').aggregate(Sum('cash'))
    outcome = outcome['cash__sum']
    net = income - outcome
    form = RecordForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('prediction:bookkeeping')
    record_list = PredictionRecord.objects.all()
    return render(request, 'prediction/bookkeeping.html', locals())

def bookdelete(request, id):
    PredictionRecord.objects.get(id=id).delete()
    return redirect('prediction:bookkeeping')

def categorysetting(request):
    categorylist = PredictionCategory.objects.all()
    form = CategoryForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('prediction:categorysetting')
    return render(request, 'prediction/categorysetting.html', locals())

def categorydelete(request, id):
    PredictionCategory.objects.get(id=id).delete()
    return redirect('prediction:categorysetting')