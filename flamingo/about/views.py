from django.shortcuts import render
from django.views import generic
from django.views.generic import TemplateView
from accounts.models import Car

class Prices(TemplateView):
    template_name = 'prices.html'

class About(TemplateView):
    template_name = 'about.html'

def Home(request):
    #Cars = Car.objects.filter(available=True)
    Cars = Car.objects.all()
    context = { 'Cars': Cars }
    return render(request, 'home.html', context)