from rest_framework import serializers
from gallery.models import Favorite, Photo


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ('id', 'description', 'image', 'author', 'created_at')
        read_only_fields = ('id')


class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = ('id', 'user', 'photo', 'created_at', 'is_deleted')
        read_only_fields = ('id')
