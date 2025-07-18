from django.db import models

# Create your models here.

class Type(models.Model):
    nom = models.CharField(max_length=50)

    def __str__ (self):
        return self.nom
    
class Catégorie(models.Model):
    nom = models.CharField(max_length=50)
    image = models.ImageField(upload_to='imagesCategories', null=True, blank=True)
    feminin = models.BooleanField()
    def __str__ (self):
        return self.nom
    

class Article(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    prix = models.IntegerField()
    quantite_stock = models.IntegerField()
    image = models.ImageField(upload_to='imagesArticles', null=True, blank=True)
    categorie = models.ForeignKey(
        Catégorie, 
        on_delete=models.CASCADE,
        null=True
        )
    type = models.ForeignKey(Type, null=True, on_delete=models.CASCADE)

    def __str__ (self):
        return f"{self.name} - {self.prix} XAF"
    
class ValiderCommande(models.Model):
    nom = models.CharField(max_length=150)
    email = models.EmailField()
    address = models.CharField(max_length=250)
    ville = models.CharField(max_length=50)
    pays = models.CharField(max_length=50)
    items = models.CharField(max_length=800)
    total = models.CharField(max_length=200)
    date_de_commande = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_de_commande']

    def __str__(self):
        return self.nom