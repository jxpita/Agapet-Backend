
from django.urls import path
from .views import (
    ActividadCreateView,
    ActividadListView,
    ActividadUpdateView,
    ActividadDetailView,
    ActividadesSemanalesView,
)

urlpatterns = [
    path('createactividad', ActividadCreateView.as_view()),
    path('listactividades', ActividadListView.as_view()),
    path('updateactividades/<int:pk>', ActividadUpdateView.as_view()),
    path('detailactividad/<int:pk>', ActividadDetailView.as_view()),

    path('actividadessemanales', ActividadesSemanalesView.as_view()),
]