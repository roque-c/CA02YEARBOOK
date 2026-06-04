from django.shortcuts import render
from .models import Student
from django.views import generic

# Create your views here.

def home(request):
    return render(request, 'yearbook/index.html')


def about(request):
    return render(request, 'yearbook/about_us.html')

class StudentListView(generic.ListView):
    model = Student
    
class StudentDetailView(generic.DetailView):
    model = Student
