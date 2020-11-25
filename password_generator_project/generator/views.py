from django.shortcuts import render
import random
import string

def home(request):
    return render(request, 'generator/home.html')

def about(request):
    return render(request, 'generator/about.html')

def password(request):
    tPassword = ''
    passwordLenghth = int(request.GET.get('passwordLength'))
    character = list(string.ascii_lowercase)
    if request.GET.get('uppercase'):
        character.extend(list(string.ascii_uppercase))
    if request.GET.get('numbers'):
        character.extend(list('1234567890'))
    if request.GET.get('special'):
        character.extend(list('!@#$%^&*()_+=-{}~[]'))

    for idx in range(passwordLenghth):
        tPassword += random.choice(character)

    return render(request, 'generator/password.html', {'password':tPassword})

