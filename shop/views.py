from django.views.generic.base import TemplateView
from shop.models import Product, Category
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from . import serializers


class MainView(TemplateView):
    template_name = 'index.html'


class ProductListView(ListCreateAPIView):
    model = Product
    serializer_class = serializers.ProductSerializer
    queryset = Product.objects.all()
    paginate_by = 100


class ProductDetailView(RetrieveUpdateDestroyAPIView):
    model = Product
    serializer_class = serializers.ProductSerializer
    queryset = Product.objects.all()
    lookup_field = 'id'


class CategoryListView(ListCreateAPIView):
    model = Category
    serializer_class = serializers.CategorySerializer
    queryset = Category.objects.all()
    paginate_by = 100


class CategoryDetailView(RetrieveUpdateDestroyAPIView):
    model = Category
    serializer_class = serializers.CategorySerializer
    queryset = Category.objects.all()
    lookup_field = 'id'