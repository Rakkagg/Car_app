from django.shortcuts import render
from django.http import JsonResponse
from .models import Car


def display_cars(request):
    color = request.GET.get('color')
    if color:
        cars = Car.objects.filter(carColor__iexact=color)
    else:
        cars = Car.objects.all().order_by('carPosition')
    return render(request, 'car_list.html', {"cars": cars})
