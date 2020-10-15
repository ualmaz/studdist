from django.shortcuts import render
from .serializers import TableSerializer
from rest_framework import generics
from .models import Table

class TableCreateSerializer(generics.ListCreateAPIView):
    queryset = Table.objects.all()
    serializer_class = TableSerializer
