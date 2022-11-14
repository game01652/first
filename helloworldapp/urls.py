from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.helloworldfunction, name='helloworldfunction'),
    path('form', views.form, name='form'),
    path('index/', views.index, name='index'),
]