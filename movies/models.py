from django.db import models

class Movie(models.Model):
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)
    release_date = models.DateField()
    created_by = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.name
