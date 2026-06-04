from django.contrib import admin

from .models import Memory, Student, Teacher, Event, EventImage

#admin.site.register(Memory)
#admin.site.register(Student)
#admin.site.register(Teacher)
#admin.site.register(Event)
#admin.site.register(EventImage)
#Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name','date_of_birth', 'biography', 'quote', 'song')
    list_filter = ('first_name','last_name')

    fieldsets =(
        (None, {
            'fields':('first_name','last_name','date_of_birth')
        }),
        ('About',{
            'fields': ('profile_picture', 'biography','quote','song')
        })
    )
admin.site.register(Student, StudentAdmin)

class TeacherAdmin(admin.ModelAdmin):
    list_display = ('title','last_name','first_name','description')
    list_filter = ('first_name','last_name', 'title')

admin.site.register(Teacher, TeacherAdmin)

class EventImageInline(admin.TabularInline):
    model = EventImage
    extra = 0

class EventAdmin(admin.ModelAdmin):
    list_display = ('name','description','event_date')
    list_filter = ('name','event_date')

    inlines = [EventImageInline]

admin.site.register(Event, EventAdmin)

class MemoryAdmin(admin.ModelAdmin):
    list_display = ('title','name','email','text','image','pub_date')
    list_filter = ('title','name','pub_date')
    
admin.site.register(Memory,MemoryAdmin)

class EventImageAdmin(admin.ModelAdmin):
    list_display = ('event','image','caption')
    list_filter = ('event','caption')
    
admin.site.register(EventImage,EventImageAdmin)