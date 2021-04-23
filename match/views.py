from django.shortcuts import render
from .models import Match
from human.models import Human
from .serializers import MatchSerializer, MatchDetailSerializer
from rest_framework import generics, permissions
from rest_framework.parsers import MultiPartParser


class MatchList(generics.ListAPIView):

    serializer_class = MatchSerializer
    queryset = Match.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    

class MatchRetrieve(generics.RetrieveAPIView):
    
    serializer_class = MatchDetailSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_object(self):
        return Human.objects.get(pk=self.kwargs['pk']).match
