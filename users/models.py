from django.db import models

from django.contrib.auth.models import User
from django.db import models
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='profile_pics')
    image = models.ImageField(default='media/profile_pics/default.png', upload_to='profile_pics')
    date_of_birth = models.CharField(max_length=12, default=' ')
    address = models.CharField(max_length=50, default=' ')
    city_town = models.CharField(max_length=50, default=' ')
    country = models.CharField(max_length=50, default=' ')
    
    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'

