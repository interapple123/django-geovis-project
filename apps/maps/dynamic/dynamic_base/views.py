from django.shortcuts import render, HttpResponse

# Create your views here.


def dynamic_base(request):
    return render(request, "dynamic_base.html")
