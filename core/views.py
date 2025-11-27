from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *


class IndexView(TemplateView): 
    template_name = "index.html" 

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['servicos'] = Servico.objects.order_by('?').all()
        context['funcionarios'] = Funcionario.objects.all()
        # Recursos
        recursos = Recurso.objects.all()

        context['recursos'] = recursos
        context['metade'] = recursos.count() // 2        
        return context



