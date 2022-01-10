from django.shortcuts import render
from .models import Movie
from rest_framework import serializers, viewsets

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'name', 'genre', 'duration', 'release_date')
        
class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
