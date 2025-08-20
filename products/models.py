from django.db import models

# Create your models here.
class Item(models.Model):
    item_name = models.CharField(max_length=150)
    item_price = models.DecimalField(max_digits=10, decimal_places=2)
    item_description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.item_name)


class RestaurantInfo(models.Model):
    name = models.CharField(max_length=200, default="My Restaurant")
    address = models.TextField()

    def __str__(self):
        return self.name