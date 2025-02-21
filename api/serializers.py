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


class ItemSerializer(serializers.ModelSerializer):
    category = CategoryNameSerializer()
    class Meta:
        model = models.Item
        fields = ('id','name','category','img','slug')
        
class ItemWithFiles(serializers.ModelSerializer):
    item = ItemSerializer()
    class Meta:
        model = models.ItemFile
        fields = ('id','item','file')
