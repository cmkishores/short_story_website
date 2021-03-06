from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model


class Story(models.Model):
	

	#genre choice field for story
	GENRE = [ 
		('CD','Comedy'),
		('AC','Action'),
		('DR','Drama'),
		('HR','Horror'),
		('KD','Kids'),
		('MY','Mythology'),
	]
	
	

	#overriding Meta for setting permission

	class Meta:
		verbose_name = "Storie"
		permissions = [

			('prime_member',"Can read the stories"),
			
			]
	
	name = models.CharField(max_length=50)
	author = models.CharField(max_length=30)
	release_year = models.CharField(max_length=4)
	genre = models.TextField(max_length=20,choices=GENRE)
	created_at = models.DateTimeField(auto_now_add=True, editable=False, null=False, blank=False)
	cover = models.ImageField(upload_to='cover/', blank=True)
	story = models.TextField()
	owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

	


	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('story',args=[str(self.id)])


# Create your models here.
