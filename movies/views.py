from django.shortcuts import render
from .models import Movie
from rest_framework import serializers, viewsets
from config.get_client_ip import get_client_ip
from rest_framework.response import Response
from rest_framework import status

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'name', 'genre', 'duration', 'release_date')
        
class CreateMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'name', 'genre', 'duration', 'release_date', 'created_by')

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset().filter(created_by=get_client_ip(request))
        serialized = MovieSerializer(queryset, many=True)
        return Response(serialized.data)

    def create(self, request, *args, **kwargs):
        request.data['created_by']=get_client_ip(request)
        serialized = CreateMovieSerializer(data=request.data)
        if not serialized.is_valid():
            return Response(status = status.HTTP_400_BAD_REQUEST, data = serialized.errors)
        else:
            serialized.save()
            serialized = MovieSerializer(serialized.data)
            return Response(status = status.HTTP_201_CREATED, data = serialized.data)
