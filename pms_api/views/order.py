from rest_framework import generics
from rest_framework import status as res_status
from drf_spectacular.utils import extend_schema
from rest_framework.response import Response


from pms_api.serializer import OrderRefundSerializer, OrderSerializer
from core.models import OrderRefund, Order

@extend_schema(tags=["Order Refund"])
class OrderRefundListCreateView(generics.ListCreateAPIView):
    queryset = OrderRefund.objects.all()
    serializer_class = OrderRefundSerializer

@extend_schema(tags=["Order Refund"])
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

    def update(self, request, *args, **kwargs):
        # Get the order instance
        order = self.get_object()

        # Only update status and last_update_by
        status = request.data.get('status', None)
        last_update_by = request.user  

        if status is not None:
            order.status = status
        order.last_update_by = last_update_by

        # Save the updated order
        order.save()

        # Return the updated order instance
        serializer = self.get_serializer(order)
        return Response(serializer.data, status=res_status.HTTP_200_OK)

