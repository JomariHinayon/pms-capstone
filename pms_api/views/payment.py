from rest_framework import generics
from drf_spectacular.utils import extend_schema

from core.models import Payment
from pms_api.serializer import PaymentSerializer

@extend_schema(tags=["Payment"])
class PaymentListCreateView(generics.ListCreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

@extend_schema(tags=["Payment"])
class PaymentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer