# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import	*

# Register your models here.
class Pregunta_1_Inline(admin.StackedInline):
	model = Pregunta_1
	max_num = 1
	can_delete = False
	filter_horizontal = ('socio','tema')

class Pregunta_2_Inline(admin.TabularInline):
	model = Pregunta_2
	extra = 1
	max_num = 4

class Pregunta_3_Inline(admin.StackedInline):
	model = Pregunta_3
	max_num = 1
	can_delete = False
	filter_horizontal = ('grupo',)

class Pregunta_4_Inline(admin.StackedInline):
	model = Pregunta_4
	max_num = 1
	can_delete = False
	filter_horizontal = ('grupo_beneficiario','tema')

class Pregunta_5a_Inline(admin.StackedInline):
	model = Pregunta_5a
	max_num = 1
	can_delete = False
	filter_horizontal = ('socio','tema')

class Pregunta_5c_Inline(admin.StackedInline):
	model = Pregunta_5c
	max_num = 1
	can_delete = False
	fieldsets = [
		('Innovación 1', {'fields' : ('organizacion_1','papel_1')}),
		('Innovación 2', {'fields' : ('organizacion_2','papel_2')}),
	]
	filter_horizontal = ('papel_1','papel_2')
	class Media:
		css = {
            'all': ('css/admin.css',)
        }
	
class Pregunta_5d_Inline(admin.StackedInline):
	model = Pregunta_5d
	max_num = 1
	can_delete = False
	fieldsets = [
		(None, {'fields' : ('innovacion_1','categoria_1')}),
		(None, {'fields' : ('innovacion_2','categoria_2')}),
	]
	filter_horizontal = ('categoria_1','categoria_2')

class Pregunta_5e_Inline(admin.StackedInline):
	model = Pregunta_5e
	max_num = 1
	can_delete = False	
	fieldsets = [
		(None, {'fields' : ('fuente_1','categoria_fuente_1')}),
		(None, {'fields' : ('fuente_2','categoria_fuente_2')}),
	]
	filter_horizontal = ('categoria_fuente_1','categoria_fuente_2')

class Pregunta_6a_Inline(admin.StackedInline):
	model = Pregunta_6a
	max_num = 1
	can_delete = False
	filter_horizontal = ('tema',)

class Pregunta_6c_Inline(admin.StackedInline):
	model = Pregunta_6c
	max_num = 1
	can_delete = False
	fieldsets = [
		('Innovación 1', {'fields' : ('organizacion_1_6c','papel_1_6c')}),
		('Innovación 2', {'fields' : ('organizacion_2_6c','papel_2_6c')}),
	]
	filter_horizontal = ('papel_1_6c','papel_2_6c')

class Pregunta_6d_Inline(admin.StackedInline):
	model = Pregunta_6d
	max_num = 1
	can_delete = False
	fieldsets = [
		(None, {'fields' : ('innovacion_1','categoria_1')}),
		(None, {'fields' : ('innovacion_2','categoria_2')}),
	]
	filter_horizontal = ('categoria_1','categoria_2')


class Pregunta_6e_Inline(admin.StackedInline):
	model = Pregunta_6e
	max_num = 1
	can_delete = False
	fields = (('conocimiento_1','categoria_innovacion_1'),('categoria_conocimiento_1'),('conocimiento_2','categoria_innocavion_2'),('categoria_conocimiento_2'))
	filter_horizontal = ('categoria_conocimiento_1','categoria_conocimiento_2')	

class Pregunta_7a_Inline(admin.StackedInline):
	model = Pregunta_7a
	extra = 1
	max_num = 3
	filter_horizontal = ('seleccion',)	

class Pregunta_7b_Inline(admin.StackedInline):
	model = Pregunta_7b
	max_num = 1
	can_delete = False
	filter_horizontal = ('seleccion',)	

class Pregunta_8_Inline(admin.StackedInline):
	model = Pregunta_8
	max_num = 1
	can_delete = False
	fields = (('organizacion','territorio'),('periodo','profundidad'),('tema'))	

class Pregunta_9_Inline(admin.TabularInline):
	model = Pregunta_9
	extra = 7
	max_num = 7
	can_delete = False
	# fieldsets = [
	# 	(None, {'fields' : ('tema','prioridad','papel')}),
	# 	('Auto-evaluación de la capacidad de la organización', {'fields' : ('conocimiento','experiencia')}),
	# ]

class Pregunta_11_Inline(admin.TabularInline):
	model = Pregunta_11
	extra = 7
	max_num = 7
	can_delete = False

class EntrevistaAdmin(admin.ModelAdmin):
	fieldsets = [
		('Información de la persona entrevistada', {'fields' : (('nombre','posicion'),('email','organizacion'),('departamento','telefono'),('fecha',))}),
	]
	inlines = [Pregunta_1_Inline, Pregunta_2_Inline, Pregunta_3_Inline, Pregunta_4_Inline, 
			   Pregunta_5a_Inline, Pregunta_5c_Inline, Pregunta_5d_Inline, Pregunta_5e_Inline,
			   Pregunta_6a_Inline, Pregunta_6c_Inline,Pregunta_6d_Inline,Pregunta_6e_Inline,
			   Pregunta_7a_Inline,Pregunta_7b_Inline,Pregunta_8_Inline,Pregunta_9_Inline,Pregunta_11_Inline]

admin.site.register(Entrevista,EntrevistaAdmin)

