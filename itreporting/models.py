from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Issue(models.Model):
    course = models.CharField(max_length=100, default='No Course', choices=[('Cyber Security', 'Cyber Security'), ('Smart Computing', 'Smart Computing'), ('Computer Science', 'Computer Science')])
    module = models.CharField(max_length=100, default='No Module')
    room = models.CharField(max_length=100)
    urgent = models.BooleanField(default=False)
    details = models.TextField()
    date_submitted = models.DateTimeField(default=timezone.now)
    description = models.TextField()
    author = models.ForeignKey(User, related_name='issues', on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.type} Issue in {self.room}'
    
    def get_absolute_url(self):
        return reverse('itreporting:issue-detail', kwargs={'pk': self.pk})
        
    