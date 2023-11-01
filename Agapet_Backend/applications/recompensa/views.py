from django.shortcuts import render
from rest_framework import viewsets
from .models import Recompensa
from .serializer import RecompensaSerializer
# otras importaciones
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

class RecompensaList(APIView):
    def get(self, request):
        recompensa = Recompensa.objects.all()
        serializer = RecompensaSerializer(recompensa, many=True)
        return Response(serializer.data)
