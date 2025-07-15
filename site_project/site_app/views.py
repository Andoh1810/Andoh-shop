from django.shortcuts import render,get_object_or_404, redirect
from .models import *
from .form import CustomUserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
# Create your views here.



def home(request):
    categories = Catégorie.objects.all()
    return render(request, 'pages/home.html', {'categories':categories})

def about(request):
    return render(request, 'pages/about.html')

def contact(request):
    return render(request, 'pages/contact.html')

def catalogue(request):
    articles = Article.objects.all().order_by('name', '-categorie')
    return render(request, 'pages/catalogue.html', {'articles':articles})

def detail(request, id):
    article = get_object_or_404(Article, id=id)
    articles = Article.objects.all()
    return render(request, 'pages/detail.html', {'article':article, 'articles':articles})

def categorie(request, id):
    cat = get_object_or_404(Catégorie,id=id)
    articles = Article.objects.filter(categorie=cat)
    return render(request, 'pages/categorie.html', {'articles':articles, 'categorie':cat})

def detail_categorie(request, id):
    article = get_object_or_404(Article, id=id)
    articles = Article.objects.all()
    categories = Catégorie.objects.all()
    return render(request, 'pages/detail_categorie.html', {'article':article, 'articles':articles, 'categories':categories})

def inscription(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('connexion')
    else:
        form = CustomUserCreationForm()
    return render(request, 'pages/inscription.html', {'form':form})        

def connexion(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Nom d\'utilisateur ou mot de passe incorrecte!')
    return render(request, 'pages/connexion.html')

def deconnexion(request):
    logout(request)
    return redirect('home')

def accueil(request):
    return render(request, 'pages/accueil.html')

def panier(request):
    return render(request, 'pages/panier.html')
