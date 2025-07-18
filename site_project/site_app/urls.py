"""
URL configuration for site_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('catalogue/', views.catalogue, name='catalogue'),
    path('article<int:id>/', views.detail, name='detail'),
    path('categorie<int:id>/', views.categorie, name='categorie'),
    path('article_det<int:id>/', views.detail_categorie, name='detail_categorie'),
    path('inscription/', views.inscription, name='inscription'),
    path('connexion', views.connexion, name='connexion'),
    path('deconnexion', views.deconnexion, name='deconnexion'),
    path('', views.accueil, name='accueil'),
    path('panier/', views.panier, name='panier'),
    path('confirmation/', views.confirmation, name='confirmation'),
]
