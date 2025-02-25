from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import models
from . import serializers
from rest_framework.generics import ListAPIView
from rest_framework import status
from rest_framework.exceptions import ValidationError

def index(request):
    return HttpResponse("<h1 style='text-align:center'>Home</h1>")

class CatagoriesList(ListAPIView):
    serializer_class = serializers.CategorySerializer
    model = models.Category
    queryset = models.Category.objects.all()
    
class ItemList(ListAPIView):
    serializer_class = serializers.ItemSerializer
    queryset = models.Item.objects.all()

    def get_queryset(self):
        queryset = super().get_queryset()
        slug = self.kwargs.get('slug')
        if slug:
            try:
                category = models.Category.objects.get(slug = slug)
                queryset = queryset.filter(category=category)
            except category.DoesNotExist:
                return HttpResponse("Bad request")
                queryset = models.Item.objects.none()  # Return an empty list if the category doesn't exist.
        return queryset

class ItemWithFiles(ListAPIView):
    serializer_class = serializers.ItemSerializer

    def get_queryset(self):
        slug = self.kwargs.get('slug')    
        data = models.Item.objects.filter(slug=slug).prefetch_related('files')
        if not data.exists():  # Eğer hiç kayıt yoksa
            raise ValidationError({"Ýalňyşlyk": "Bu slug bilen item ýok!"})
        return data 
    
    