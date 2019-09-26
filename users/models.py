from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
	
	TYPE = [
			('RD','Reader'),
			('WR','Writer'),
	]
	user_type = models.CharField(max_length=20,choices=TYPE)

# Create your models here.
