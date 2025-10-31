from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request, "main/index.html")

def static_map(request):
    return render(request, "main/static_map.html")

def dynamic_map(request):
    return render(request, "main/dynamic_map.html")
