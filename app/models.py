from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    item_name = models.CharField(max_length=200)
    item_description  = models.TextField()
    item_price = models.IntegerField()
    
    item_img = models.ImageField(default='placehold.jpg',upload_to='profile_pics')
    
    
    def __str__(self):
         return self.item_name 