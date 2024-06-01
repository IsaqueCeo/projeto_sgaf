from django.urls import path
from .views import perfil_professor

urlpatterns = [
    path('', perfil_professor, name='perfil-professor'),

]
