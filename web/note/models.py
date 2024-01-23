from django.db import models

# Create your models here.
class note(models.Model):
    user_name = models.CharField(max_length = 20)
    title = models.CharField(max_length = 50)
    category = models.CharField(max_length = 20)
    contents = models.TextField()