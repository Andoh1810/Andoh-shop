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
    

