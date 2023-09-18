from .models import Alumnos
from rest_framework import serializers


class AlumnosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Alumnos
        fields = ["id","nombre","cursos"]
