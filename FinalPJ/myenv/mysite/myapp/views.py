# myapp/views.py

from django.shortcuts import render

#�index page view (main page)
def index(request):
    return render(request, 'myapp/index.html')  # index.html을 렌더링합니다.

#game page view
def game(request):
    return render(request, 'myapp/game.html') 
