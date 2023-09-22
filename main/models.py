from django.db import models
from django.contrib.auth.models import User

class Item(models.Model):
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    description = models.TextField() # untuk warna dan bahan 
    in_laundry = models.BooleanField(default=False) # menandakan jika sedang di laundry atau tidak
    user = models.ForeignKey(User, on_delete=models.CASCADE)