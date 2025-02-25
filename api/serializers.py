from rest_framework import serializers
from . import models

class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Banner
        fields = '__all__'

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
        

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.OrderItem
        fields = ['item']

class OrderSerializer(serializers.ModelSerializer):
    items = serializers.ListField(child=serializers.IntegerField(), write_only=True)  
    order_date = serializers.DateTimeField()  

    class Meta:
        model = models.Order
        fields = ['username', 'phone', 'order_date', 'items']

    def create(self, validated_data):
        items_data = validated_data.pop('items', []) 
        order = models.Order.objects.create(**validated_data)  

        order_items = [models.OrderItem(order=order, item_id=item_id) for item_id in items_data]
        models.OrderItem.objects.bulk_create(order_items) 
        return order
    
