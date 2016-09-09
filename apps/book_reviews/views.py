from django.contrib.auth.decorators import login_required
from django.template.loader import get_template
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.template import RequestContext
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import random
from .forms import RegisterForm

# from django.shortcuts import render
# from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
  # Create your views here.

def login(request):
  form = AuthenticationForm(request.POST)
  form2 = UserCreationForm
  print form.is_valid()
  print form.errors
  return render(request, "book_reviews/index_forms.html", {"form":form, "form2":form2()})

def register(request):
  form = AuthenticationForm
  form2 = UserCreationForm(request.POST)
  print form2.is_valid()
  print form2.errors
  return render(request, "book_reviews/index_forms.html", {"form":form(), "form2":form2})

def index_forms(request):
  form = AuthenticationForm
  form2 = UserCreationForm
  return render(request, "book_reviews/index_forms.html", {"form":form(), "form2":form2()})

def show_users(request):
    User.objects.create_user(first_name="eelay", last_name="Tsai", username=str( random.randint(0, 100)))
    users = User.objects.all()
    return render(request, "book_reviews/show_users.html", {'users':users})

def index(request):
    form = RegisterForm()
    context = {'regForm': form }
    return render(request, "book_reviews/index.html", context)

# def register(request):
#     if request.method == "POST":
#         myform = RegisterForm(request.POST)
#         #user = request.POST['alias']
#         print myform.is_valid()
#         print myform.errors
#         if myform.is_valid():
#             myform.save()
#             alias = request.POST['alias']
#             return render(request, "book_reviews/register_success.html", {'alias':  alias})
#             #     return HttpResponse(html)
#             # return HttpResponseRedirect("/book_reviews/register_success/", {'alias': request.POST['alias']})
#     else:
#         form = RegisterForm()
#         context = {
#             'regForm': form
#         }
#         return render(request, "/book_reviews/register/", context)
#
def register_success(request):
    return render(request, "book_reviews/register_success.html", {'alias':  alias})
# def index(request):
#     name = "eelay"
#     html = "<html><body>Hi %s, this seems to have worked!</body></html>" % name
#     return HttpResponse(html)
