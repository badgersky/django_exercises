from django.shortcuts import render


def greet_user(request):
    if request.method == 'GET':
        return render(request, 'form_training/greet_user.html')
    elif request.method == 'POST':
        name = request.POST['name']
        surname = request.POST['surname']
        greetings = f'Hello {name.title()} {surname.title()}'
        return render(request, 'form_training/greet_user.html', context={'greetings': greetings})
