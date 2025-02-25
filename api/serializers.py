from rest_framework import serializers
from . import models



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = '__all__'
        
class CategoryNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = ('name','slug')

class ItemFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ItemFile
        fields = ['file']  # Sadece dosya URL'sini döndürürüz

class ItemSerializer(serializers.ModelSerializer):
    files = ItemFileSerializer(many=True, read_only=True)  # Item'a bağlı dosyaları liste olarak alıyoruz

    class Meta:
        model = models.Item
        fields = ['id', 'name', 'img', 'category', 'price', 'description', 'slug', 'files'] 