from rest_framework.serializers import ModelSerializer
from shop.models import Product, Category


class ProductSerializer(ModelSerializer):

    class Meta:
        model = Product


class CategorySerializer(ModelSerializer):

    class Meta:
        model = Category