from django.shortcuts import render
from .models import Restaurant

# Create your views here.
def home(request):
    """
    Home page that fetches the restaurant details
    and display the details.
    """
    restaurant = Restaurant.objects.first()
    return render(request, "homepage.html", {"restaurant": restaurant})