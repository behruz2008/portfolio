from django.db import models

# Create your models here.


class Men(models.Model):
    ism_sharif = models.CharField(max_length=200)
    yil = models.DateField()
    manzil = models.CharField(max_length=200)
    rasm = models.ImageField(upload_to='rasmlar', null=True, blank=True)
    email = models.CharField(max_length=30, null=True, blank=True)
    telefon = models.CharField(max_length=13)
    men_haqimda = models.TextField()
    resume = models.FileField(upload_to="rezyumealrim")
   
    def __str__(self):
        return self.ism_sharif
    
    class Meta:
        verbose_name = "Men_haqimda"
        verbose_name_plural = "Men haqimda"
        
        
# servizlar degan model ochilib, unga nom va malumot degan textfield o'zgaruvchi beriladi


class Portfolio(models.Model):
    rasm = models.ImageField(upload_to='portfolio_rasmlar', null=True, blank=True)
    nom = models.CharField(max_length=200)
    link = models.CharField(max_length=1000)
    malumot = models.TextField()
    def __str__(self):
        return self.nom
    
    class Meta:
        verbose_name = "Portfolio"
        verbose_name_plural = "Portfolio"
        
        
class Blog(models.Model):
    rasm = models.ImageField(upload_to='portfolio_rasmlar', null=True, blank=True)
    mavzu = models.CharField(max_length=200)
    malumot = models.TextField()
    sana = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.mavzu
    
    
    class Meta:
        verbose_name = "blog"
        verbose_name_plural = "Blog"
    