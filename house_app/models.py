from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class House(models.Model):
    name=models.CharField(max_length=40)
    location=models.CharField(max_length=25)
    price=models.IntegerField()
    bedrooms=models.IntegerField()
    bathrooms=models.IntegerField()
    toilets=models.IntegerField()
    sitting_room=models.IntegerField()
    swimming_pool=models.BooleanField()
    image1=models.ImageField(upload_to='houses',default='default.jpg')
    dealer=models.ForeignKey(User,on_delete=models.CASCADE)
        

    def format_price(self):
        return "{:,}".format(self.price)


class WareHouse(models.Model):
    name=models.CharField(max_length=40)
    location=models.CharField(max_length=25)
    price=models.IntegerField()
    dealer=models.ForeignKey(User,on_delete=models.CASCADE)
    space=models.IntegerField()
    
    

    def format_price(self):
        return "{:,}".format(self.price)


class Land(models.Model):
    location=models.CharField(max_length=25)
    price=models.IntegerField()
    name=models.TextField()
    dealer=models.ForeignKey(User,on_delete=models.CASCADE)
    space=models.IntegerField()
    
    

    def format_price(self):
        return "{:,}".format(self.price)






