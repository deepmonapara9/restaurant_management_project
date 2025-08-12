from django.urls import path
from .views import *

urlpatterns = [
    path('api/menu', MenuAPIView.as_view(), name='menu-list'),
]