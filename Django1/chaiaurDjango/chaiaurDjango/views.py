from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    return render(request, 'website/index.html')  # noqa: S106

def about(request):
    return HttpResponse('This is about page')  # noqa: S106

def contact(request):
    return HttpResponse('This is contact page')  # noqa: S106