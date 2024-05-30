from rest_framework import serializers
from .models import Movie

class MovieListSerializer(serializers.ModelSerializer):
    # id = serializers.IntegerField(read_only=True)
    # movie_name = serializers.CharField(max_length=100)
    class Meta:
        model = Movie
        fields = '__all__'
        # fields = ['movie_name','release_year','director','actors','region']

class MovieDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'