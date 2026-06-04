from django.shortcuts import render

from django.views import generic

from .models import Event, EventImage
# Create your views here.

def home(request):
    return render(request, 'index.html')


class EventListView(generic.ListView):
    model = Event



