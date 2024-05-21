from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Car

def display_cars(request):
    cars = Car.objects.all().order_by('carPosition')
    return render(request, 'car_list.html', {"cars": cars})

def sorting_red_cars(request):
    red_cars = Car.objects.filter(carColor__iexact='red').order_by('carPosition')
    return render(request, 'car_list.html', {'cars': red_cars})

def sorting_blue_cars(request):
    blue_cars = Car.objects.filter(carColor__iexact='blue').order_by('carPosition')
    return render(request, 'car_list.html', {'cars': blue_cars})

@csrf_exempt
def post_switch_car(request):
    if request.method == 'POST':
        new_positions = request.POST.getlist('car[]')
        for index, car_id in enumerate(new_positions):
            car = Car.objects.get(id=car_id)
            car.carPosition = index
            car.save()
        return JsonResponse({'message': 'Car positions updated successfully'})
    return JsonResponse({'error': 'Invalid request'}, status=400)
