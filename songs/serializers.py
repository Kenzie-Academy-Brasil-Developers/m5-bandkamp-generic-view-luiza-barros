from rest_framework import serializers
from .models import Song


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ["title", "duration", "id", "album_id"]
        read_only_fields = ["album_id"]

    def create(self, validated_data):
        return Song.objects.create(**validated_data)
