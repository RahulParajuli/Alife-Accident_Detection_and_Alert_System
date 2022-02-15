import email
from urllib import request
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login , logout
from matplotlib.style import context
import requests

API_key='1815471bae9d4f2ba54bd93544987656'
category = 'Accidents'

# Create your views here.
def index(request):
    return render(request, "index.html")

def profile(request):
    return HttpResponse("hello this is profile")

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password1']
        password2 = request.POST['password2']

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        login(request,user)
        return render(request, 'index.html')
    else:
        return HttpResponse('entered else of regsiter')

def login_view(request):
    return render(request, "login.html")

def register_view(request):
    return render(request, "register.html")

def road_cond(request):
    return render(request, "roadcondition.html")

def login_check(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username , password=password)

        if user is not None:
            login(request,user)
            # messages.success(request, 'Login successful')
            return redirect( '/dashboard')
        else:
            #  messages.error(request, 'Login Failed.')
             return render(request, 'index.html')
    else:
        # messages.warning(request, 'Please enter username and password')
        return redirect()
    
def features(request):
    return render(request, "features.html")

def contact(request):
    return render(request, "contact.html")

def about(request): 
    return render(request, "about.html")

def traffic_update(request):
    return render(request, "elements.html")

def news(request):
    url = "https://newsapi.org/v2/everything?lang=en&q=accident&apiKey=1815471bae9d4f2ba54bd93544987656"
    url2 = "https://newsapi.org/v2/everything?lang=en&q=accident&sortBy=publishedAt&apiKey=1815471bae9d4f2ba54bd93544987656"
    

    response = requests.get(url)
    response2 = requests.get(url2)
    data = response.json()
    data2 = response2.json()
    articles = data['articles']
    articles2 = data2['articles']

    context = {
        'articles' : articles, 'articles2': articles2

    }

    return render(request, "blog.html", context)

def dashboard(request):
    return render(request, "dashboard.html")