from .views import RecompensaList
from django.urls import path


urlpatterns = [
    path('recompensa', RecompensaList.as_view()), 
]
