from django.shortcuts import render
from django.http import HttpResponse, HttpRequest


def greet_user(request):
    if request.method == 'GET':
        return render(request, 'form_training/greet_user.html')
    elif request.method == 'POST':
        name = request.POST['name']
        surname = request.POST['surname']
        greetings = f'Hello {name.title()} {surname.title()}'
        return render(request, 'form_training/greet_user.html', context={'greetings': greetings})


def convert_temperature(request):
    if request.method == 'GET':
        return render(request, 'form_training/temp_convector.html')
    elif request.method == 'POST':
        temp = float(request.POST['degrees'])
        button = request.POST['convertionType']
        if button == 'celcToFahr':
            converted = temp * 1.8 + 32
            return render(request, 'form_training/temp_convector.html', context={'temp': converted})
        elif button == 'FahrToCelc':
            converted = (temp - 32) * 0.5556
            return render(request, 'form_training/temp_convector.html', context={'temp': converted})