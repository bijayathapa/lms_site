from django.db import models

# Create your models here.


class Course(models.Model):
    name = models.CharField(max_length=255, null=True)
    duration = models.IntegerField(null=True)
    details = models.TextField(null=True)
    cost = models.IntegerField(null=True)
    course_image = models.ImageField(null = True, blank = True )
    
    def __str__(self):
        return self.name
    

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url