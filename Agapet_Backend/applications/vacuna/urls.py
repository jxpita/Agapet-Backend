from .views import VacunasMascotaViewSet, Mascotaupdate
from django.urls import path

from .views import VacunaCreateView, VacunaUpdateView, VacunaListView, VacunaDetailView

urlpatterns = [
    path('mascota', VacunasMascotaViewSet.as_view()),
    path('actualizar/<str:pk>/', Mascotaupdate.as_view()),

    #vacunas
    path('createvacuna', VacunaCreateView.as_view()),
    path('updatevacuna/<int:pk>', VacunaUpdateView.as_view()),
    path('listvacuna', VacunaListView.as_view()),
    path('vacunadetail/<int:pk>', VacunaDetailView.as_view())
    
]
