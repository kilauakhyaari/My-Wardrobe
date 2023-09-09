from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    description = models.TextField() # untuk warna dan bahan 
    in_laundry = models.BooleanField(default=False) # menandakan jika sedang di laundry atau tidak