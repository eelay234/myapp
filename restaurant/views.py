from django.shortcuts import render

# Create your views here
from .models import *
# Create your views here.
def index(request):
    Context = {
        'pizzas': Pizza.objects.all()
     }

    return render(request, "restaurant/index.html", Context)
