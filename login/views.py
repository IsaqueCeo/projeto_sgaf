from django.shortcuts import render
from . models import Login

def login(request):
    if request.method == 'POST':
        login = Login.POST()
