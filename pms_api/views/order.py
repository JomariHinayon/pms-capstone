from rest_framework import generics
from drf_spectacular.utils import extend_schema

from pms_api.serializer import OrderRefundSerializer, OrderSerializer
from core.models import OrderRefund, Order

@extend_schema(tags=["Order"])
class OrderRefundListCreateView(generics.ListCreateAPIView):
    queryset = OrderRefund.objects.all()
    serializer_class = OrderRefundSerializer

@extend_schema(tags=["Order"])
class OrderRefundDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderRefund.objects.all()
    serializer_class = OrderRefundSerializer

@extend_schema(tags=["Order"])
class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

@extend_schema(tags=["Order"])
class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
