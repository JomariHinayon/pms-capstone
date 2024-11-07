from rest_framework import serializers
from core.models import Account, Product, OrderRefund, Order, Payment, Category
from rest_framework.response import Response


class AccountSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Account
        fields = ('username', 'email', 'password')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'description']

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()  

    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'price', 'stock', 'category', 'image']

class AccountDetailsSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Account
        fields = "__all__"

class OrderRefundSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderRefund
        fields = ['id', 'user', 'order', 'reason', 'refund_amount', 'status', 'request_date', 'approval_date', 'comments']


class OrderSerializer(serializers.ModelSerializer):
    user = AccountDetailsSerializer()
    product = ProductSerializer(many=True)  

    class Meta:
        model = Order
        fields = ['id', 'user', 'product', 'quantity', 'request_date', 'status', 'approval_date', 'comments', 'last_update_by']

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = [
            'id',
            'user',
            'order',
            'amount',
            'payment_method',
            'status',
            'transaction_id',
            'payment_date',
            'comments'
        ]
        read_only_fields = ['id', 'payment_date']