from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    director_name = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    synopsis = models.TextField()
    image = models.ImageField(upload_to='movies/', blank=True, null=True)

    def __str__(self):
        return self.title
