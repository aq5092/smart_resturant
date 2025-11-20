from .models import BotUser, Role, Restaurant, Employee, Menu, MenuType,Order,OrderMenu
from rest_framework import serializers

class BotUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = BotUser
        fields = "__all__"

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = "__all__"

class RestauranSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = "__all__"

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"

class MenuSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields ="__all__"
    
class MenuTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuType
        fields = "__all__"

class OrderSerilazer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"

class OrderMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderMenu
        fields = "__all__"
