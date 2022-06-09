from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from django.views import generic
from django.core.paginator import Paginator
from tabela.models import Dataset, Source
from tabela.forms import datasetForm, sourceForm

# Create your views here.

def update_option(request, pk):
    my_instance = get_object_or_404(Dataset, pk=pk)
    form = datasetForm(instance=my_instance)
    if request.method == 'POST':
        form = datasetForm(request.POST, instance=my_instance)
        #if form.is_valid():
        form.save()
    return render(request, 'tabela/update.html', {'form': form})

def load_sources(request):
    sources = Source.objects.all()
    return render(request, 'tabela/source_list_options.html', {'sources': sources})

def add_source(request):
    form = sourceForm()
    if request.method == 'POST':
        form = sourceForm(request.POST)
        if form.is_valid():
            source_tipo = form.cleaned_data['tipo']
            new_source = Source(tipo=source_tipo)
            new_source.save()
        return render(request, 'tabela/add_source.html', {'form': form})
    elif (request.method == 'GET'):
        return render(request, 'tabela/add_source.html', {'form': form})

def index(request):
    p = Paginator(Dataset.objects.all(), 8)
    page = request.GET.get('page')
    dataset = p.get_page(page)
    allFields = Dataset._meta.get_fields()
    return render(request, 'tabela/index.html', {'dataset': dataset, 'allFields': allFields[1:]})
