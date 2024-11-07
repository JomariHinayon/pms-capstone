from django.shortcuts import render
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from drf_spectacular.utils import extend_schema
from rest_framework.authtoken.views import ObtainAuthToken

from pms_api.serializer import AccountSerializer, AccountDetailsSerializer
from core.models import Account

@extend_schema(tags=["Account"])
class AccountListView(generics.ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountDetailsSerializer

@extend_schema(tags=["Account"])
class AccountDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountDetailsSerializer

@extend_schema(tags=["Authentication"])
class AccountRegistrationView(generics.CreateAPIView):
    queryset = Account.objects.all()  # Define the queryset for the view
    serializer_class = AccountSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)  
        
        user = serializer.save()
        user.set_password(request.data['password'])  
        user.save() 

        token, created = Token.objects.get_or_create(user=user)

        return Response({
            'message': 'User registered successfully',
            'user_id': user.id,
            'username': user.username,
            'token': token.key
        }, status=201)  

@extend_schema(tags=["Authentication"])
class AccountLoginView(APIView):
    serializer_class = AccountSerializer
    permission_classes = [permissions.AllowAny] 

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)

        if user:
            token, created = Token.objects.get_or_create(user=user)

            return Response({
                'message': 'Login successful',
                'token': token.key,
                'user_type': user.user_type
            }, status=status.HTTP_200_OK)
        else:
            return Response({
                'error': 'Invalid credentials'
            }, status=status.HTTP_401_UNAUTHORIZED)
        

@extend_schema(tags=["Authentication"])
class ObtainAuthTokenView(ObtainAuthToken):
    permission_classes = [permissions.AllowAny] 

