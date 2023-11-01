from .views import (
    CursoList,
    CursoCreateView,
    CursoUpdateView,
    CursoDetailView,
    
    TemaCursoList, 
    TemaCursoCreateView,
    TemaCursoUpdateView,
    TemaCursoDetailView,

    PreguntaList, 
    RespuestaList,
    TemaiewSet
)
from django.urls import path


urlpatterns = [

    #TEMA CURSO
    path('temas', TemaCursoList.as_view()),
    path('createtema', TemaCursoCreateView.as_view()),
    path('updatetema/<int:pk>', TemaCursoUpdateView.as_view()),
    path('detailtema/<int:pk>', TemaCursoDetailView.as_view()),

    #CURSO
    path('cursos', CursoList.as_view()),
    path('createcurso', CursoCreateView.as_view()),
    path('updatecurso/<int:pk>', CursoUpdateView.as_view()),
    path('detailcurso/<int:pk>', CursoDetailView.as_view()),

    #CURSO_REALIZADO

    path('preguntas', PreguntaList.as_view()),
    path('respuestas', RespuestaList.as_view()),
    path('tema/cursos', TemaiewSet.as_view()),
]
