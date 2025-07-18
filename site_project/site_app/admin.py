from django.contrib import admin
from .models import *
# Register your models here.

admin.site.site_header = 'Andoh-shop'

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('name','description', 'prix', 'image' , 'quantite_stock', 'categorie', 'type')
    search_fields = ('name', 'description')
@admin.register(Catégorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display = ('nom', 'image', 'feminin')
    search_fields = ('nom',)
@admin.register(Type)
class ClassAdmin(admin.ModelAdmin):
    list_display = ('nom',)
    search_fields = ('nom',)
@admin.register(ValiderCommande)
class CommandeAdmin(admin.ModelAdmin):
    list_display = ('nom','email','address','ville','pays','date_de_commande','items','total')
    search_fields = ('nom','address','ville')