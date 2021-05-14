from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse

from .models import Pasien
# Create your views here.
def index(request):
    Data = Pasien.objects.all()
    context = {
        'Data':Data,
    }
    return render(request, 'index.html', context)
