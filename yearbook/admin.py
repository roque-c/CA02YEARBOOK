from django.contrib import admin

from .models import Memory, Student, Teacher, Event, EventImage

admin.site.register(Memory)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Event)
admin.site.register(EventImage)
#Register your models here.
