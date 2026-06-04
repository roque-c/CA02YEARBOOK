from django.db import models
from django.urls import reverse

class Memory(models.Model):
    title = models.CharField(max_length=200, null=False) 
    name = models.CharField(max_length=100, help_text="Enter submitter's name", null=False)
    email = models.EmailField(max_length=254, null = False)
    text = models.TextField(max_length=1000, help_text="Enter a brief description of the memory you wish to share")
    image = models.ImageField(upload_to="memory_gallery/", max_length=100,null=True, blank = True)
    pub_date = models.DateTimeField("date published")

    class Meta:
        ordering = ['-pub_date']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """Returns the URL to access a particular memory instance."""
        return reverse('memory-detail', args=[str(self.id)])

class Student(models.Model):
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100, null=False)
    date_of_birth = models.DateField(null=True, blank=True)
    biography = models.TextField(max_length=2000, help_text="Enter a brief Biography of the student, including future aspirations")
    quote = models.CharField(max_length=500, help_text="enter a quote that represents you", null=True)
    song = models.CharField(max_length= 100, help_text="enter a song that represents your senior year", null=True)
    
    class Meta:
        ordering = ['last_name', 'first_name']
        
    def __str__(self):
        return f'{self.first_name}, {self.last_name}'

    def get_absolute_url(self):
        """Returns the URL to access a detail record for this student."""
        return reverse('student-detail', args=[str(self.id)])



class Teacher(models.Model):
    title = models.CharField(max_length=4, help_text="enter mr. ms. or mrs.",null=False)
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=200,help_text="enter a brief description of the teacher's role for the seniors", blank=False)


    class Meta:
        ordering = ['last_name', 'first_name']
        
    def __str__(self):
        return f'{self.first_name}, {self.last_name}'

    def get_absolute_url(self):
        """Returns the URL to access a detail record for this Teacher."""
        return reverse('teacher-detail', args=[str(self.id)])
    

class Event(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=2000, help_text="Enter a brief description of the Event you want to share")
    event_date = models.DateField(null=False)

    EVENT_TYPE= (
            ('t', 'Trabajo Educativo Social'),
            ('a', 'School Activity'),
            ('r', 'Random'),
            ('s', 'Sport'),
        )

    event_type = models.CharField(
            max_length=1,
            choices=EVENT_TYPE,
            blank=True,
            default='a',
            help_text='Event type',
        )
    class Meta:
        ordering = ['-event_date']

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        """Returns the URL to access a detail record for this event."""
        return reverse('event-detail', args=[str(self.id)])

def event_image_path(instance, filename):
    return f'event_gallery/event_{instance.event.id}/{filename}'

class EventImage(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='event_images')
    image = models.ImageField(upload_to=event_image_path)
    caption = models.CharField(max_length=200, blank=True)
    
    def __str__(self):
        return f'Image {self.id} of {self.event.name}'

    def get_absolute_url(self):
        """Returns the URL to access a detail record for this image."""
        return reverse('event-image-detail', args=[str(self.id)])
# Create your models here.
