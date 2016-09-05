from django.shortcuts import render
from .models import *
# Create your views here.
def index(request):
    Context = {
        'autos': Car.objects.all()
     }

    return render(request, "automobiles/index.html", Context)
