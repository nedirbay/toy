from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import models
from . import serializers
from rest_framework.generics import ListAPIView

def index(request):
    return HttpResponse("<h1 style='text-align:center'>Home</h1>")

class CatagoriesList(ListAPIView):
    serializer_class = serializers.CategorySerializer
    model = models.Category
    queryset = models.Category.objects.all()
    
class ItemList(ListAPIView):
    serializer_class = serializers.ItemSerializer
    model = models.Item
    
    def get_queryset(self):
        slug = self.kwargs.get('slug')
        queryset = models.Item.objects.all()

        if slug:
            queryset = queryset.filter(category_slug=slug)
        return queryset
        
    
    
    