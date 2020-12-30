from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='img/',default='img/None/No-img.jpg')


    def __str__(self):
        return self.title