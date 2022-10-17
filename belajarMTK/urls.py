from django.contrib import admin
from django.urls import path
from pengertian.views import indexpengertian
from rumus.views import indexrumus
from soal.views import indexsoal

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pengertian/', indexpengertian),
    path('rumus/', indexrumus), 
    path('soal/', indexsoal),
]
