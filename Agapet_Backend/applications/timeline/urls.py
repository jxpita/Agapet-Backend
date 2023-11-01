from .views import (
    FaseListView,
    FaseCreateView,
    FaseUpdateView,

    TimelineViewSet,
    AdoptanteTimelineView,
    TimelineListView,
    TimelineDetailView,
    TimelineCreateView,
    TimelineUpdateView,

    Timeline_faseListView,
    TimelineFaseCreateView,
    TimelineFaseUpdateView,
)
from django.urls import path


urlpatterns = [
    path('fases', TimelineViewSet.as_view()),
    path('adoptante/<int:pk>', AdoptanteTimelineView.as_view()),
    
    #fases
    path('faselist', FaseListView.as_view()),
    path('fasecreate', FaseCreateView.as_view()),
    path('faseupdate/<int:pk>', FaseUpdateView.as_view()),

    #timeline
    path('listtimeline', TimelineListView.as_view()),
    ########### ES UNA GUÍA
    #puedes ver información detallada del timeline y sus fases
    path('detailtimeline/<int:pk>', TimelineDetailView.as_view()),

    ##################### USAS
    #crea un timeline y se lo asigna a un adoptante y mascota, le pones un colaborador o administrador
    path('timelinecreate', TimelineCreateView.as_view()),
    #el administrador puede actualizar: descripcion, fechas de inicio y finalizacion del proceso de adopción
    path('timelineupdate/<int:pk>', TimelineUpdateView.as_view()),
    #######################


    #timelinefase
    path('listtimelinefase', Timeline_faseListView.as_view()),
    #se asigna una fase a un timeline que ya está asignado a un adoptante
    #este proceso es automático
    path('createtimelinefase', TimelineFaseCreateView.as_view()),
    
    ####################### USAS
    #se actualizan las fases asignadas a un proceso: si la fase fue aprobada, cuando inicia o termina
    path('updatetimelinefase/<int:pk>', TimelineFaseUpdateView.as_view())
    #######################3#
]
