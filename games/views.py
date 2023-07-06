from rest_framework import generics
from .serializers import GameSerializer
from .models import Game
from .permissions import OwnerOrReadOnly


class GameList(generics.ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer


class GameDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (OwnerOrReadOnly,)
    queryset = Game.objects.all()
    serializer_class = GameSerializer
