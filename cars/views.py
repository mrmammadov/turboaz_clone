from django.shortcuts import render
from django.views.generic import ListView
from cars.models import CarModel

class CarsListView(ListView):
    model = CarModel