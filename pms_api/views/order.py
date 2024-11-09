from rest_framework import generics, serializers, status
from rest_framework import status as res_status
from drf_spectacular.utils import extend_schema
from rest_framework.response import Response
from django.utils import timezone

from pms_api.serializer import OrderRefundSerializer, OrderSerializer
from core.models import OrderRefund, Order, Product, Account

@extend_schema(tags=["Order Refund"])
class OrderRefundListCreateView(generics.ListCreateAPIView):
    queryset = OrderRefund.objects.all()
    serializer_class = OrderRefundSerializer

    def get_queryset(self):
        # Filter payments to only return those related to the current user
        return OrderRefund.objects.filter(user=self.request.user)

@extend_schema(tags=["Order Refund"])
class OrderRefundDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderRefund.objects.all()
    serializer_class = OrderRefundSerializer


@extend_schema(tags=["Order"])
class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def create(self, request, *args, **kwargs):
        # Extract 'name' and 'description' fields from request data
        data = request.data.copy()
        product_name = data.get('product_name') 
        quantity = data.get('quantity') # Product title is provided as 'name'
        description = data.get('description')
        category = data.get('category')

        # Find the product by title
        product = Product.objects.filter(title=product_name).first()
        if not product:
            return Response(
                {"error": f"Product with title '{product_name}' does not exist."},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Create the order instance and add the product
        order = Order.objects.create(
            user=request.user,
            comments=description,
            quantity=quantity,
            last_update_by=request.user
        )
        order.product.add(product)

        # Serialize and return the created order
        serializer = self.get_serializer(order)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@extend_schema(tags=["Order"])
class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def update(self, request, *args, **kwargs):
        # Get the order instance
        order = self.get_object()

        # Only update status and last_update_by
        status = request.data.get('status', None)
        final_status = request.data.get('final_status', None)
        last_update_by = request.user  

        if status is not None:
            order.status = status

        if final_status is not None:
            order.final_status = final_status
            order.approval_date = timezone.now() 

        order.last_update_by = last_update_by

        # Save the updated order
        order.save()

        # Return the updated order instance
        serializer = self.get_serializer(order)
        return Response(serializer.data, status=res_status.HTTP_200_OK)

