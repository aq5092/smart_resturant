from django.contrib import admin

# Register your models here.
# admin.py
from django.contrib import admin
from .models import *

admin.site.register(BotUser)
admin.site.register(Role)
admin.site.register(Restaurant)
admin.site.register(Employee)
admin.site.register(MenuType)
admin.site.register(Menu)
admin.site.register(Order)
admin.site.register(OrderMenu)