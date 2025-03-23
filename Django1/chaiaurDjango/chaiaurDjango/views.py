from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    return render(request, 'website/index.html')  # noqa: S106

def about(request):
    return render(request,'website/about.html')  # noqa: S106

def contact(request):
    return render(request,'website/contact.html')  # noqa: S106