from django.shortcuts import render
from django.views.generic import ListView , DetailView , View
from .models import Employee
# Create your views here.

class HomeView(ListView):
    model = Employee
    template_name = "home-page.html"
