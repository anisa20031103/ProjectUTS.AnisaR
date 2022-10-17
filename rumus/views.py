from django.shortcuts import render

# Create your views here.
def indexrumus(request):
    return render(request, 'rumus.html')