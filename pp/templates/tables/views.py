from rest_framework import generics
from .models import Table
from .serializers import TableSerializer
from django.shortcuts import get_list_or_404

class TableListCreate(generics.ListCreateAPIView):
    queryset = Table.objects.all()
    serializer_class = TableSerializer

class AvailableTables(generics.ListAPIView):
    serializer_class = TableSerializer

    def get_queryset(self):
        return Table.objects.filter(available=True)
