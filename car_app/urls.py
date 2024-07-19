from django.urls import path
from . import views

urlpatterns = [
    path('', views.display_cars, name='car_list'),
    path('switch_car/', views.switch_car, name='switch_car'),
]
