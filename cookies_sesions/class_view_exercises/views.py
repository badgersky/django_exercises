from django.shortcuts import render
from django.views import View


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
    