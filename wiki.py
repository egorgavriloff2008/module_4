def slova():
    s = input("введите слово:  ")
    if s [::-1] == s:
        print(True)
    else:
        print(False)

slova()


from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('Success!!!!')




from django.urls import path
from .views import index

urlpatterns = [
    path('', index),
]
