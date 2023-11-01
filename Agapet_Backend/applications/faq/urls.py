from django.urls import path
from .views import FaqListView, FaqCreateView, FaqUpdateView, FaqDetailView

urlpatterns = [
    #path('tema', TemaList.as_view()),
    path('listpreguntas', FaqListView.as_view()),
    #path('faq/tema', FaqTemaViewSet.as_view()),
    path('createpregunta', FaqCreateView.as_view()),
    path('uodatepregunta/<int:pk>', FaqUpdateView.as_view()),
    path('detailpregunta/<int:pk>', FaqDetailView.as_view())
    
]
