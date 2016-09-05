# Create your views here.
#views.py
# from login.forms import *
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
from forms import MyRegistrationForm
from django.views.decorators.csrf import csrf_protect
from django.template import Context
from .models import Article, Comment
from forms import ArticleForm, CommentForm
from django.contrib.auth.decorators import login_required
# from django.core.context_processors import csrf
def add_comment_to_article(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.save()
            return redirect('/get/'+str(article.pk), pk=article.pk)
    else:
        form = CommentForm()
    return render(request, 'login_reg/add_comment_to_article.html', {'form': form})

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    article_pk = comment.article.pk
    comment.delete()
    return redirect('/get/'+str(article_pk), pk=article_pk)

def like_article(request, article_id):
    if article_id:
        a =  Article.objects.get(id=article_id)
        count = a.likes
        count += 1
        a.likes = count
        a.save()

        return HttpResponseRedirect('/articles/get/%s' % article_id)

def create(request):
    if request.POST:
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/articles/all')
    else:
         form = ArticleForm()

    args = {}
    args['form'] = form
    return render(request, 'login_reg/create_article.html', args)

def articles(request):
    language = "en-gb"
    session_language = "en-gb"
    if 'lang' in request.session:
        language = request.session['lang']

    if 'lang' in request.COOKIES:
        language = request.COOKIES['lang']
    return render(request, "login_reg/articles.html", {'articles': Article.objects.all(),
                                                        'language': language,
                                                        'session_language': session_language })

def article(request, article_id):
    return render(request, "login_reg/article.html", {'article': Article.objects.get(id=article_id) })

def  language(request, language="en-gb"):
      response = HttpResponse('setting language to %s' %  language)
      response.set_cookie('lang', language)
      request.session['lang'] = language
      return response

def hello(request):
    name = "eelay"
    html = "<html><body>Hi %s, this seems to have worked!</body></html>" % name
    return HttpResponse(html)

def hello_template(request):
    name = "Eelay"
    t = get_template('login_reg/hello.html')
    html = t.render(Context({'name':name}))
    return HttpResponse(html)

def hello_template_simple(request):
    name =  "EELAY"
    Context = {
        'name': name
    }
    return render(request, "login_reg/hello.html", Context)

@csrf_protect
def login(request):
    # c = {}
    # c.update(csrf(request))
    # return render_to_response('login.html', c)
    return render(request, 'login_reg/login.html')
    # return render_to_response('login_reg/login.html')

@csrf_protect
def auth_view(request):
    username =  request.POST.get('username', '')
    password =  request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/accounts/loggedin')
    else:
        return HttpResponseRedirect('/accounts/invalid')

def loggedin(request):
    return render_to_response('login_reg/loggedin.html',
                   {'full_name': request.user.username})

def invalid_login(request):
    return render_to_response('login_reg/invalid_login.html')

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/accounts/login/')

def register_user(request):
    if request.method == 'POST':
        form = MyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/accounts/register_success')
    else:
        form = MyRegistrationForm()
    args = {}
    args['form'] = form
    # print "args:"
    # print args
    return render(request, 'login_reg/register.html', args)

def  register_success(request):
    return render_to_response('login_reg/register_success.html')
# @csrf_protect
# def register(request):
#     if request.method == 'POST':
#         form = RegistrationForm(request.POST)
#         if form.is_valid():
#             user = User.objects.create_user(
#             username=form.cleaned_data['username'],
#             password=form.cleaned_data['password1'],
#             email=form.cleaned_data['email']
#             )
#             return HttpResponseRedirect('/register/success/')
#     else:
#         form = RegistrationForm()
#     variables = RequestContext(request, {
#     'form': form
#     })
#
#     return render_to_response(
#     'registration/register.html',
#     variables,
#     )
#
# def register_success(request):
#     return render_to_response(
#     'registration/success.html',
#     )
#
# def logout_page(request):
#     logout(request)
#     return HttpResponseRedirect('/')
#
# @login_required
# def home(request):
#     return render_to_response(
#     'home.html',
#     { 'user': request.user }
#     )
