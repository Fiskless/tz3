from django.shortcuts import render
from .models import Human
from .serializers import HumanSerializer
from rest_framework import generics, permissions
from rest_framework.parsers import MultiPartParser


class HumanList(generics.ListCreateAPIView):
    parser_classes = [MultiPartParser]
    serializer_class = HumanSerializer
    queryset = Human.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class HumanRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    
    serializer_class = HumanSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Human.objects.all()

