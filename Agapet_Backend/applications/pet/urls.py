from .views import (
    MascotaViewSet, 
    UsuarioMascotaViewSet,
    UsuarioMascotaView, 
    MascotaCreateView,
    MascotaUpdateView,
    MascotaListView,
    MascotaDetailView,

    AnimalListView,
    AnimalCreateView,

    VacunadoView,
    VacunadoUpdateView,
)
from rest_framework import routers
from django.urls import path


router_mascota = routers.DefaultRouter()
router_mascota.register(prefix='mascota', basename='mascota', viewset=MascotaViewSet)

urlpatterns = [
    #si no existe mandar un objeto vacío
    #
    #path('usuario/<str:pk>/', UsuarioMascotaViewSet.as_view()),
    path('usuario/<str:pk>/', UsuarioMascotaView.as_view()),

    #mascotas
    path('createmascota', MascotaCreateView.as_view()),
    path('updatemascota/<int:pk>', MascotaUpdateView.as_view()),
    path('listmascota', MascotaListView.as_view()),
    path('detailmascota/<int:pk>', MascotaDetailView.as_view()),

    ##vacunas
    path('vacunas', VacunadoView.as_view()),
    path('vacunasupdate/<int:pk>', VacunadoUpdateView.as_view()),

    #animal
    path('listanimal', AnimalListView.as_view()),
    path('createanimal', AnimalCreateView.as_view())
    
]
