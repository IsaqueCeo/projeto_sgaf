from django.shortcuts import render
from . models import Login

def login(request):
    if request.method == 'POST':
        form = LoginForm.POST()
        if form.is_valid:
            form.save()

           

        
