from django.urls import path
from .views import *

# from django.views.static.
urlpatterns = [
    path('', Curso.as_view(), name='p_inicio'),
    path('detail/<slug:slug>/',CursoDetailView.as_view(),name='curso_detail')
]
