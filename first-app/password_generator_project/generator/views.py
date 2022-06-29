from django.shortcuts import render
from django.http import HttpResponse
import random


def home(request):
    lst = list(range(6, 15))
    return render(request, 'generator/home.html', {'lst': lst})


def password(request):
    char = [chr(i) for i in range(97, 123)]

    if request.GET.get('uppercase'):
        char.extend([chr(i) for i in range(65, 91)])

    psw = ''
    length = int(request.GET.get('length'))
    for i in range(length):
        psw += random.choice(char)
    return render(request, 'generator/password.html', {'password': psw})
