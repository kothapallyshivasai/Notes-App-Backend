from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Notes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)  
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True) 
    last_modified = models.DateTimeField(auto_now=True)  

    def __str__(self):
        return f"{self.user}, {self.title}"
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/profile/', blank=True)
