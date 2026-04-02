from django.shortcuts import render

def dribble_home(request):
    return render(request, 'dribble.html')
