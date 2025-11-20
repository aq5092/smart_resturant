from django.shortcuts import render
from .models import BotUser, Role, Restaurant, Employee, Menu, MenuType,Order,OrderMenu
from rest_framework import generics, viewsets   
from .serializers import BotUserSerializer, RoleSerializer, RestauranSerializer, EmployeeSerializer, MenuSerialzer, MenuTypeSerializer, OrderSerilazer, OrderMenuSerializer
from rest_framework.permissions import AllowAny

class BotUserViewset(viewsets.ModelViewSet):
    serializer_class = BotUserSerializer
    queryset = BotUser.objects.all()
    permission_classes = [AllowAny]

class RoleViewset(viewsets.ModelViewSet):
    serializer_class = RoleSerializer
    queryset = Role.objects.all()

class RestaurantViewset(viewsets.ModelViewSet):
    serializer_class = RestauranSerializer
    queryset = Restaurant.objects.all()

class EmployeeViewset(viewsets.ModelViewSet):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()

class MenuViewset(viewsets.ModelViewSet):
    serializer_class = MenuSerialzer
    queryset = Menu.objects.all()

class MenuTypeViewset(viewsets.ModelViewSet):
    serializer_class = MenuTypeSerializer
    queryset = MenuType.objects.all()

class OrderViewset(viewsets.ModelViewSet):
    serializer_class = OrderSerilazer
    queryset = Order.objects.all()

class OrderMenuViewset(viewsets.ModelViewSet):
    serializer_class = OrderMenuSerializer
    queryset = OrderMenu.objects.all()
# Create your views here.
