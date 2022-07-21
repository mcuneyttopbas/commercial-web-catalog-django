from catalog.models import Product, Collection
from rest_framework import serializers

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = "__all__"

class CollectionSerializer(serializers.ModelSerializer):

    class Meta: 
        model = Collection
        fields = "__all__"