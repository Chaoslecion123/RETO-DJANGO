from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from .models import Curso as mis_cursos
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class Curso(TemplateView):
    template_name = 'cursos/cursos.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cursos"] =  mis_cursos.objects.filter(estado=True)
        return context

    
    

class Index_principal(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(Index_principal,
                        self).get_context_data(**kwargs)
        context['cursos'] = mis_cursos.objects.filter(estado=True)
        return context


class CursoDetailView(LoginRequiredMixin,DetailView):
    template_name = 'cursos/detail.html'
    model = mis_cursos