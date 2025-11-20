from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BotUserViewset, RoleViewset, RestaurantViewset, EmployeeViewset, MenuViewset, MenuTypeViewset, OrderViewset, OrderMenuViewset
router = DefaultRouter()
router.register(r'botusers', BotUserViewset, basename='botusers')
router.register(r'roles', RoleViewset, basename='roles')
router.register(r'restaurants', RestaurantViewset, basename='restaurants')
router.register(r'employees', EmployeeViewset, basename='employees')
router.register(r'menus', MenuViewset, basename='menus')
router.register(r'menutyepes', MenuTypeViewset, basename='menutypes')
router.register(r'orders', OrderViewset, basename='orders')
router.register(r'ordermenus', OrderMenuViewset, basename='ordermenus')

urlpatterns = [
    path('', include(router.urls))
]