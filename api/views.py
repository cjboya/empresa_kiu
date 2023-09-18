from .models import Alumnos
from .serializers import AlumnosSerializer
from rest_framework import viewsets, permissions
from rest_framework.response import Response


class AlumnosViewSet(viewsets.ModelViewSet):
    queryset = Alumnos.objects.all()
    #permission_classes = [permissions.AllowAny]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = AlumnosSerializer
    #http_method_names = ['get']
    #http_method_names = ['get', 'post', 'put', 'delete']
