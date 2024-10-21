from rest_framework import generics
from drf_spectacular.utils import extend_schema

from pms_api.serializer import ProductSerializer
from core.models import Product


@extend_schema(tags=["Product"])
class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

@extend_schema(tags=["Product"])
class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    