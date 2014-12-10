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
		print sector
		return context
		