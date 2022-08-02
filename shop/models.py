from django.db import models

# Create your models here.

class Catergory(models.Model):
    name = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now=True)


    class Meta:
        
        ordering = [ '-date_added' ]

    def __str__(self):
        return self.name
    

class Product(models.Model):

    title = models.CharField(max_length=100)
    price = models.FloatField(default=0.0)
    description = models.TextField(max_length=500)
    category = models.ForeignKey(Catergory, related_name='categorie', on_delete=models.CASCADE)
    image = models.CharField(max_length=5000)
    date_added = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = [ '-date_added' ]
    
    
    def __str__(self):
        return self.title
    
    

