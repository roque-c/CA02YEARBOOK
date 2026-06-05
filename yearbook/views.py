from django.shortcuts import render
from django.views import generic
from django.utils import timezone
from .models import Student, Event, EventImage, Teacher, Memory
from .forms import MemoryForm
# Create your views here.



def home(request):
    # Get the latest 3 memories, ordered by most recent pub_date
    latest_memories = Memory.objects.order_by('-pub_date')[:3]
    context = {
        'latest_memories': latest_memories,
    }
    return render(request, 'yearbook/index.html', context)

def about(request):
    return render(request, 'yearbook/about_us.html')

def add_memory(request):
    memories = Memory.objects.order_by('-pub_date')[:10]
    success = False

    if request.method == 'POST':
        form = MemoryForm(request.POST, request.FILES)
        if form.is_valid():
            memory = form.save(commit=False)
            memory.pub_date = timezone.now()
            memory.save()
            success = True
            # Clear form after success
            form = MemoryForm()
    else:
        form = MemoryForm()

    context = {
        'memories': memories,
        'form': form,
        'success': success,
    }
    return render(request, 'yearbook/memory_wall.html', context)

class MemoryListView(generic.ListView):
    model = Memory
    
class TeacherListView(generic.ListView):
    model = Teacher
    
class TeacherDetailView(generic.DetailView):
    model = Teacher

class StudentListView(generic.ListView):
    model = Student
    
class StudentDetailView(generic.DetailView):
    model = Student

class EventListView(generic.ListView):
    model = Event

class EventDetailView(generic.DetailView):
    model = Event

