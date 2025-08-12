from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.respones import Response
from rest_framework import status

# Create your views here.
class MenuAPIView(APIView):
    def get(self, request):
        menu_data = [
            {"name": "Margherita Pizza", "description": "Classic cheese and tomato pizza", "price": 8.99},
            {"name": "7 chessy Pizza", "description": "It's chessy", "price": 9.00},
            {"name": "FarmVilaa Pizza", "description": "It contains different different veggies", "price": 10.00},
        ]

        return Response(menu_data, status=status.HTTP_200_OK)