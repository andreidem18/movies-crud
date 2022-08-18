from django.db import models
from softdelete.models import SoftDeleteObject

class Movie(SoftDeleteObject, models.Model):
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)
    release_date = models.DateField()
    created_by = models.CharField(max_length=20, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
