from django.db import models


# Create your models here.
class Card(models.Model):
    title = models.CharField(max_length=32)
    image = models.ImageField(upload_to="images", null=True)
    description = models.CharField(max_length=32)
    url = models.URLField()
    username = models.CharField(max_length=128)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.title
