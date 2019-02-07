from django.db import models

# Create your models here.
class Videos(models.Model):
    title= models.CharField(max_length=100)
    slug= models.SlugField()
    description= models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    upload= models.FileField(upload_to='my_video/',null=True)

    def __str__(self):
        return self.title

    def snippet(self):
        return self.description[:50] + '....'