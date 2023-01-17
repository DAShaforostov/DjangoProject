from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def leo(request):
    return HttpResponse('Знак зодиака - Лев')

def sagi(request):
    return HttpResponse('Знак зодиака - Стрелец')

def cancer(request):
    return HttpResponse('Знак зодиака - Рак')

def libra(request):
    return HttpResponse('Знак зодиака - Весы')

def capri(request):
    return HttpResponse('Знак зодиака - Козерог')