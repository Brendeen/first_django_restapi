from rest_framework import serializers
from .models import Game


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['id', 'title', 'description', 'owner', 'created_at']
        model = Game
