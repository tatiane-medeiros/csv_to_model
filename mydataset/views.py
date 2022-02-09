from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.views import generic
from mydataset.models import Dataset

# Create your views here.

def index(request):
    # return HttpResponse("Funcionou!!!")
    # template = loader.get_template('index.html')
    dataset = Dataset.objects.all()
    return render(request, 'mydataset/index.html', {'dataset': dataset})
