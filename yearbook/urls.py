from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('class_of_2026/', views.StudentListView.as_view(), name='students'),
    path('class_of_2026/<int:pk>', views.StudentDetailView.as_view(),name='student-detail')
]
