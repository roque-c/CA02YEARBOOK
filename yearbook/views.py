from django.shortcuts import render
from .models import Student
from django.views import generic

from django.views import generic

from .models import Event, EventImage
# Create your views here.

def home(request):
    return render(request, 'yearbook/index.html')


class EventListView(generic.ListView):
    model = Event


def about(request):
    return render(request, 'yearbook/about_us.html')

class StudentListView(generic.ListView):
    model = Student
    
class StudentDetailView(generic.DetailView):
    model = Student
