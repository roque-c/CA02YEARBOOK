from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('class_of_2026/', views.StudentListView.as_view(), name='students'),
    path('class_of_2026/<int:pk>', views.StudentDetailView.as_view(), name='student-detail'),
    path('events/', views.EventListView.as_view(), name='events'),
    path('events/<int:pk>', views.EventDetailView.as_view(), name='event-detail'),
    path('teachers/', views.TeacherListView.as_view(), name='teachers'),
    path('teachers/<int:pk>', views.TeacherDetailView.as_view(), name='teacher-detail'),
    path('add_memory/', views.add_memory, name='add_memory'),
    path('memory-wall/', views.MemoryListView.as_view(), name='memories')
]
