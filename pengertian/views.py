from django.shortcuts import render

# Create your views here.
def indexpengertian(request):
    return render(request, 'pengertian.html')