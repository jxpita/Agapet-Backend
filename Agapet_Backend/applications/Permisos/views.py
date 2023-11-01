from django.shortcuts import render

# Django Rest Framework
from rest_framework.views import APIView
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
import jwt, datetime

from .serializer import PermisoSerializer

#Models

from .models import Permiso

from rest_framework.generics import get_object_or_404
from rest_framework import status

from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    UpdateAPIView,
    RetrieveUpdateAPIView
)

class PermisosView(ListAPIView):
    serializer_class = PermisoSerializer
    def get_queryset(self):
        return Permiso.objects.all()

class PermisosCreateView(CreateAPIView):
    serializer_class = PermisoSerializer

class PermisosUpdateView(RetrieveUpdateAPIView):
    serializer_class = PermisoSerializer
    queryset = Permiso.objects.all()