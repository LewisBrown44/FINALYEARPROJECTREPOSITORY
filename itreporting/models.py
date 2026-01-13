from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Issue(models.Model):
    course = models.CharField(max_length=100, default='No Course', choices=[('Cyber Security', 'Cyber Security'), ('Smart Computing', 'Smart Computing'), ('Computer Science', 'Computer Science')])
    module = models.CharField(max_length=100, default=' ')
    code = models.CharField(max_length=100, default=' ')
    credit = models.CharField(max_length=100, default=' ')
    category = models.CharField(max_length=100, default=' ')
    availability = models.CharField(max_length=100, default=' ', choices=[('Open for Registration', 'Open for Registration'), ('Closed for Registration', 'Closed for Registration')])
    courses_allowed_to_register = models.BooleanField(default=False)
    date_submitted = models.DateTimeField(default=timezone.now)
    description = models.TextField()
    author = models.ForeignKey(User, related_name='issues', on_delete=models.CASCADE)
    
    def get_absolute_url(self):
        return reverse('itreporting:issue-detail', kwargs={'pk': self.pk})
        
    
    