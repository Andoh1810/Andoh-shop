from django.shortcuts import render,get_object_or_404, redirect
from .models import *
from .form import CustomUserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
import json
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

    if request.method == 'GET':
        name = request.GET.get('rechercher_produitCata')
        if name is not None:
            articles = Article.objects.filter(name__icontains = name)

    return render(request, 'pages/catalogue.html', {'articles':articles})

def detail(request, id):
    article = get_object_or_404(Article, id=id)
    articles = Article.objects.all()
    return render(request, 'pages/detail.html', {'article':article, 'articles':articles})

def categorie(request, id):
    cat = get_object_or_404(Catégorie,id=id)
    articles = Article.objects.filter(categorie=cat)

    if request.method == 'GET':
        name = request.GET.get('rechercher_produitCate')
        if name is not None:
            articles = Article.objects.filter(name__icontains = name)

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
    if request.method == 'POST':
        nom = request.POST.get('nom')
        email = request.POST.get('email')
        address = request.POST.get('Address')
        ville = request.POST.get('ville')
        pays = request.POST.get('pays')
        items = request.POST.get('items')
        total = request.POST.get('total')
        commande = ValiderCommande(nom=nom, email=email, address=address, ville=ville, pays=pays, items=items, total=total)
        commande.save()

        # Mise à jour du stock
        panier = json.loads(items)
        for item_id, article_data in panier.items():
            quantite = int(article_data[0])
            try:
                article = Article.objects.get(id=int(item_id))
                if article.quantite_stock >= quantite:
                    article.quantite_stock -= quantite
                    article.save()
                else:
                    print(f"Stock insuffisant pour l'article {article.name}")
            except Article.DoesNotExist:
                print(f"Article ID {item_id} non trouvé")

        return redirect('confirmation')

    return render(request, 'pages/panier.html')

def confirmation(request):
    info = ValiderCommande.objects.all()[:1]
    for item in info:
        nom = item.nom
    
    return render(request, 'pages/confirmation.html', {'nom':nom})
