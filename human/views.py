from django.shortcuts import render
from .models import Human
from .serializers import HumanSerializer
from rest_framework import generics, permissions
from rest_framework.parsers import MultiPartParser


class HumanList(generics.ListCreateAPIView):
    media_type = 'multipart/form - data'
    serializer_class = HumanSerializer
    queryset = Human.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class HumanRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = HumanSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return Human.objects.filter(pk=self.kwargs['pk'])
