from django.shortcuts import render


def all_chai(request):
    return render(request, 'arunchai/all_chai.html')  # noqa: S106
# Create your views here.
