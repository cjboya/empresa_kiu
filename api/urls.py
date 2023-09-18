
#from django.urls import URLPattern
from rest_framework import routers
from .views import AlumnosViewSet

router = routers.DefaultRouter()

router.register('api/alumno', AlumnosViewSet, "alumnos")

urlpatterns = router.urls
