from .views import (
    RegisterView,
    UserView, 
    UserList, 
    Userupdate, 
    UserFilter, 
    UserDetailView, 
    RegisterSecondView, 
    UserDeleteView, 
    UserApiLista,
    UserUpdateView,
    UserRetrieveUpdateView,
    AdminApiLista,
    ColaboradorApiLista,
    RegisterColaboradorView,
    RegisterAdoptanteView,
    ResgisterAdministradorView,
    RecibePermisoView,
    AdoptanteApiLista,
    CustomTokenObtainPairView,
    AdoptanteDetailView,
    AdminDetailView,
    ColaboradorDetailView,
    AdministradorUpdateView,
    ColaboradorUpdateView,
    AdoptanteUpdateView,
    RecibePermisoUpdateView,

    NumeroAdoptantesView,
)
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('register', RegisterView.as_view()), 
    #path('registrar', RegisterSecondView.as_view()), 
    path('login', CustomTokenObtainPairView.as_view()),
    path('token/refresh', TokenRefreshView.as_view()),
    path('data', UserView.as_view()), 
    path('list', UserList.as_view()), 
    path('update', Userupdate.as_view()), 

    path('updateuser/<int:pk>',UserRetrieveUpdateView.as_view()),

    #REVISAR 
    #Lista de usuarios por tipo
    path('adminlist', AdminApiLista.as_view()),
    path('colaboradorlist', ColaboradorApiLista.as_view()),
    path('adoptanteslist', AdoptanteApiLista.as_view()),

    #Registro de usuarios por tipo
    path('registercolaborador', RegisterColaboradorView.as_view()), 
    path('registeradoptante', RegisterAdoptanteView.as_view()), 
    path('registeradministrador', ResgisterAdministradorView.as_view()),

    #Detalle de usuario individual por tipo
    path('adoptantedetail/<int:pk>', AdoptanteDetailView.as_view()),
    path('admindetail/<int:pk>', AdminDetailView.as_view()),
    path('colaboradordetail/<int:pk>', ColaboradorDetailView.as_view()),

    #Actualización de usuarios por tipo
    path('updateadmin/<int:pk>', AdministradorUpdateView.as_view()),
    path('updatecolaborador/<int:pk>', ColaboradorUpdateView.as_view()),
    path('updateadoptante/<int:pk>', AdoptanteUpdateView.as_view()),

    #Agregar y Actualizar Permisos de Colaboradores
    path('recibepermiso', RecibePermisoView.as_view()),
    path('recibepermisoupdate/<int:pk>', RecibePermisoUpdateView.as_view()),

    #Datos de la Gráfica
    path('numeroadoptantes', NumeroAdoptantesView.as_view()),





#   REVISAR
    #Filtro de usuarios
    path('filtro/<str:user>', UserFilter.as_view(), name='filtro'),
    #Detalle de usuarios
    path('detail/<int:pk>',UserDetailView.as_view()),
    #path('usuario/<int:pk>', UserIndividual.as_view()),
    #path('usuarios/', UserIndividual.as_view()),

    #Eliminar usuarios, se deben inactivar
    path('delete/<int:pk>',UserDeleteView.as_view()),
    path('update/<int:pk>',UserUpdateView.as_view()),
    path('usuarioslist', UserApiLista.as_view()),
]
