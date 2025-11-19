# models.py
from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid


# Telegram bot userlari (bot_users)
class BotUser(models.Model):
    id = models.BigIntegerField(primary_key=True)  # Telegram user ID
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.id})"


# Rollar
class Role(models.Model):
    name = models.CharField(max_length=100, unique=True)  # masalan: admin, manager, waiter, cook

    def __str__(self):
        return self.name


# Restoran
class Restaurant(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    bot_user = models.ForeignKey(BotUser, on_delete=models.CASCADE, related_name='restaurants')
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


# Xodimlar (employees)
class Employee(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='employees')
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, related_name='employees')
    bot_user = models.ForeignKey(BotUser, on_delete=models.CASCADE, related_name='employee_profile')

    def __str__(self):
        return f"{self.bot_user.name} - {self.role}"


# Menu turlari (masalan: Taomlar, Ichimliklar, Desertlar)
class MenuType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Menu (taomlar)
class Menu(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    menu_type = models.ForeignKey(MenuType, on_delete=models.CASCADE, related_name='menus')
    price = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='menu/', blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} - {self.price} so'm"


# Buyurtma (orders)
class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)  # masalan: "1-stol", "Delivery #123"
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, related_name='orders')
    created_at = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    status = models.CharField(max_length=50, default='new')  # new, cooking, ready, delivered, cancelled

    def __str__(self):
        return f"#{self.id} - {self.name}"


# Buyurtmadagi taomlar (order items)
class OrderMenu(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='order_items')
    quantity = models.PositiveIntegerField(default=1)
    price_at_time = models.DecimalField(max_digits=12, decimal_places=2)  # sotuv vaqtidagi narx

    def __str__(self):
        return f"{self.menu.name} x{self.quantity}"

    def total(self):
        return self.quantity * self.price_at_time