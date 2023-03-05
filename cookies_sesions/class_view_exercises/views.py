from django.shortcuts import render
from django.views import View
from django.http import HttpResponse


class GreetUser(View):
    def get(self, request):
        return render(request, 'class_view_exercises/get_name_surname.html')

    def post(self, request):
        name = request.POST['name']
        surname = request.POST['surname']
        return render(request, 'class_view_exercises/get_name_surname.html', context={
            'name': name.title(),
            'surname': surname.title(),
        })


class TemperatureConversion(View):
    def get(self, request):
        return render(request, 'class_view_exercises/temp_converter.html')

    def post(self, request):
        conversion_type = request.POST.get('conversionType')
        if conversion_type == 'CelcToFahr':
            fahrenheit = float(request.POST['degrees']) * 1.8 + 32
            return HttpResponse(f'{fahrenheit}')
        else:
            celsius = (float(request.POST['degrees']) - 32) * 0.5556
            return HttpResponse(f'{celsius}')
