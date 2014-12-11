# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *

# Create your views here.
class IndexView(ListView):
	template_name = 'index.html'
	model = Sector

	def get_context_data(self,**kwargs):
		context = super(IndexView, self).get_context_data(**kwargs)
		contador_org = Organizacion.objects.count()
		sector = {}
		for x in Sector.objects.all():
			cont_org = Organizacion.objects.filter(sector=x).count()
			sector[x.nombre] = cont_org
		context['contador_sector'] = sector

		tema = {}
		for y in Tema.objects.all():
			contador_pregunta1 = Pregunta_1.objects.filter(tema=y).count()
			tema[y.tema] = contador_pregunta1
		context['contador_tematica'] = tema
		
		prueba = {}
		for i in Sector.objects.all():
			conteo = Pregunta_1.objects.filter(entrevistado__organizacion__sector=i).count()
			prueba[i.nombre] = conteo
		context['proyectos'] = prueba
			

		return context

		