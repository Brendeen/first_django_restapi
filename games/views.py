from rest_framework import generics
from .serializers import GameSerializer
from .models import Game


class GameList(generics.ListAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer


class GameDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
