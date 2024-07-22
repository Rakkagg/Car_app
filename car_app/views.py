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


def switch_car(request):
    if request.method == 'POST':
        new_positions = request.POST.getlist('car[]')
        cars_to_update = [Car(id=car_id, carPosition=index) for index, car_id in enumerate(new_positions)]
        Car.objects.bulk_update(cars_to_update, ['carPosition'])
        return JsonResponse({'message': 'Car positions updated successfully'})
    return JsonResponse({'error': 'Invalid request'}, status=400)
