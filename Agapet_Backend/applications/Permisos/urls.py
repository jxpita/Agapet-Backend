from .views import(
    PermisosView,
    PermisosCreateView,
    PermisosUpdateView,

)

from django.urls import path


urlpatterns = [
    path('permisos', PermisosView.as_view()),
    path('create', PermisosCreateView.as_view()),
    path('updatepermisos/<int:pk>', PermisosUpdateView.as_view()),
]
