from django.urls import path
from . import views

urlpatterns = [
    path('', views.display_cars, name='display_cars'),
    path('sorting_red_cars/', views.sorting_red_cars, name='sorting_red_cars'),
    path('sorting_blue_cars/', views.sorting_blue_cars, name='sorting_blue_cars'),
    path('post_switch_car/', views.post_switch_car, name='post_switch_car'),
]
