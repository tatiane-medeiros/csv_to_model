from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from mydataset.models import Dataset

# Create your views here.

def index(request):
    # return HttpResponse("Funcionou!!!")
    # template = loader.get_template('index.html')
    return render(request, 'mydataset/index.html')
