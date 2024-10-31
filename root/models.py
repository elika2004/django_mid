from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=100)
    firt_name=models.CharField( max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField( max_length=254)
    status=models.BooleanField(default=False)

    def __str__(self):
        return self.username

class Testimonials(models.Model):
    contact=models.CharField(max_length=100)
    image=models.ImageField(upload_to='agent',default='defult.jpg')
    user=models.ForeignKey(User, on_delete=models.CASCADE)

class Pros(models.Model):
    title=models.CharField( max_length=50)
    status=models.BooleanField(default=False) 


class Prices(models.Model):
    title=models.CharField( max_length=50)
    price=models.IntegerField()
    pros=models.ManyToManyField(Pros)
    status=models.BooleanField(default=False) 

class FQA(models.Model):
     title=models.CharField( max_length=50)
     answer=models.CharField( max_length=50)

class Services(models.Model):
     title=models.CharField( max_length=50)
     desc=models.CharField( max_length=50)
     status=models.BooleanField(default=False) 

class Services_two(models.Model):
     title=models.CharField( max_length=50)
     desc=models.CharField( max_length=50)
     status=models.BooleanField(default=False) 