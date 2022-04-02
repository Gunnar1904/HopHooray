from django.db import models
from django.conf import settings

class Beer(models.Model):
    name = models.CharField(max_length=200, null=True)
    origin = models.CharField(max_length=200, null=True)
    beertype = models.CharField(max_length=200, null=True)
    amount = models.PositiveIntegerField(null=True)
    price = models.PositiveIntegerField(null=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='beer_owned')
    added_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def total_value(self):
        return self.amount * self.price


        
        
        


        

