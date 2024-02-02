from django.urls import path, include
from rest_framework.routers import DefaultRouter
from modulos.views.perfil_view import UsuarioViewSet, NombreUsuarioViewSet, CreateUserView, UsuarioColaboradorViewSet, UsuarioClienteViewSet
from modulos.views.alimento_view import AlimentoViewSet
from modulos.views.producto_view import ProductoViewSet
from modulos.views.raza_view import RazaViewSet
from modulos.views.notificacion_view import NotificacionViewSet
from modulos.views.tiposervicio_view import TipoServicioViewSet
from modulos.views.servicio_view import ServicioViewSet
from modulos.views.tipoevento_view import TipoEventoViewSet
from modulos.views.evento_view import EventoViewSet
from modulos.views.eventointeres_view import EventoInteresViewSet
from modulos.views.tipoanimal_view import TipoAnimalViewSet
from modulos.views.animal_view import AnimalesPorPerfilViewSet, AnimalViewSet
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="AGAPET modulos Swagger",
        default_version="v1",
        description="Documentacion",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="jxpita@espol.edu.ec"),
        license=openapi.License(name="ESPOL License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

router = DefaultRouter()

router.register(r"usuario", UsuarioViewSet)
router.register(r'nombreusuario', NombreUsuarioViewSet, basename='nombreusuario')
router.register(r"usuariocolaborador", UsuarioColaboradorViewSet)
router.register(r"usuariocliente", UsuarioClienteViewSet)


router.register(r"alimento", AlimentoViewSet)
router.register(r"producto", ProductoViewSet)
router.register(r"raza", RazaViewSet)

router.register(r"notificacion", NotificacionViewSet)

router.register(r"tiposervicio", TipoServicioViewSet)
router.register(r"servicio", ServicioViewSet)

router.register(r"tipoevento", TipoEventoViewSet)
router.register(r"evento", EventoViewSet)
router.register(r"eventointeres", EventoInteresViewSet)

router.register(r"tipoanimal", TipoAnimalViewSet)
router.register(r"animal", AnimalViewSet)
router.register(r'animal/usuarioresponsable', AnimalesPorPerfilViewSet)
router.register(r'animal/usuarioresponsable/(?P<perfil_id>\d+)', AnimalesPorPerfilViewSet, basename='usuarioresponsable')

urlpatterns = [
    path("", include(router.urls)),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    path('create-user/', CreateUserView.as_view(), name='create-user'),
]
