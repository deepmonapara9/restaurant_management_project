from django.db import models

# Create your models here.
class RestaurantLocation(models.Model):
    """
    Model to store the location of the restaurant.
    """
    address = models.CharField(max_length=255, default="Tasty Bites")
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)
    opening_hours = models.JSONField(max_length=100)

    def __str__(self):
        return f"{self.address}, {self.city}, {self.state} - {self.zip_code}"