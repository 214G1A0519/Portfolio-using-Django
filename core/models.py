from django.db import models

# Create your models here.
 
class About(models.Model):
    short_description=models.TextField()
    description=models.TextField()
    image=models.ImageField(upload_to='about')
    
    class Meta:
        verbose_name="About me"
        verbose_name_plural="About me"
    def __str__(self):
        return "About me"

#Service Model
class Service(models.Model):
    name=models.CharField(max_length=100,verbose_name="Service name")
    description=models.TextField(verbose_name="About Service")
    
    def __str__(self):
        return self.name

#recent Work Model
class RecentWork(models.Model):
    title = models.CharField(max_length=100,verbose_name="Work title")
    image=models.ImageField(upload_to="works")
    
    def __str__(self):
        return self.title

class Client(models.Model):
    name=models.CharField(max_length=100, verbose_name="Client name")
    description=models.TextField(verbose_name="Clent say")
    image=models.ImageField(upload_to="clients", default="default.png")
    
    def __str__(self):
        return self.name
    