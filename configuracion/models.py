# -*- coding: utf-8 -*-
from django.db import models
from django.template.defaultfilters import slugify
from smart_selects.db_fields import ChainedForeignKey

# Create your models here.

class Departamento(models.Model):
	departamento  = models.CharField(max_length=50)
	slug = models.SlugField(editable=False)

	def __unicode__(self):
		return self.departamento
	
	def save(self, *args, **kwargs):
		if not  self.id:
			self.slug = slugify(self.departamento)
		super(Departamento, self).save(*args, **kwargs)


class Municipio(models.Model):
	municipio  = models.CharField(max_length=50)
	departamento = models.ForeignKey(Departamento)
	slug = models.SlugField(editable=False)

	def __unicode__(self):
		return self.municipio
	
	def save(self, *args, **kwargs):
		if not  self.id:
			self.slug = slugify(self.municipio)
		super(Municipio, self).save(*args, **kwargs)

class Status_Legal(models.Model):
	nombre = models.CharField(max_length=200)

	def __unicode__(self):
		return self.nombre

	class Meta:
		verbose_name = 'Status Legal'
		verbose_name_plural = 'Status Legal'

class Sector(models.Model):
	nombre  = models.CharField(max_length=200)

	def __unicode__(self):
		return self.nombre

	class Meta:
		verbose_name = 'Sector'
		verbose_name_plural = 'Sectores'

		
class Organizacion(models.Model):
	nombre = models.CharField(max_length=200)
	status_legal = models.ForeignKey(Status_Legal)
	anno_fundacion = models.DateField(verbose_name='Año de fundación')
	dueno = models.CharField(verbose_name='Dueño, Presidente, Director',max_length=200)
	numero_activistas = models.IntegerField(verbose_name='Numero de activistas o miembros')
	direccion = models.CharField(max_length=200)
	departamento = models.ForeignKey(Departamento)
	#municipio = models.ForeignKey(Municipio)
	municipio = ChainedForeignKey(
								Municipio,
	 							chained_field="departamento", 
	 					 		chained_model_field="departamento",
	 					 		show_all=False, auto_choose=True)
	telefono = models.IntegerField()
	fax = models.IntegerField()
	email = models.EmailField()
	sector = models.ForeignKey(Sector)
	slug = models.SlugField(editable=False)

	def __unicode__(self):
		return self.nombre

	def save(self, *args, **kwargs):
		if not  self.id:
			self.slug = slugify(self.nombre)
		super(Organizacion, self).save(*args, **kwargs)

	class Meta:
		verbose_name = 'Organización'
		verbose_name_plural = 'Organizaciones'

class Estado(models.Model):
	estado = models.CharField(max_length=50)

	def __unicode__(self):
		return self.estado

class Ubicacion(models.Model):
	ubicacion = models.CharField(max_length=50)

	def __unicode__(self):
		return self.ubicacion

class Socio(models.Model):
	socio = models.CharField(max_length=100)

	def __unicode__(self):
		return self.socio

class Tema(models.Model):
	tema = models.CharField(max_length=100)

	def __unicode__(self):
		return self.tema

class Grupo(models.Model):
	nombre = models.CharField(max_length=100)

	def __unicode__(self):
		return self.nombre

class Grupo_Beneficiario(models.Model):
	nombre = models.CharField(max_length=100)

	def __unicode__(self):
		return self.nombre

	class Meta:
		verbose_name = 'Grupo Beneficiario'
		verbose_name_plural = 'Grupos Beneficiarios'

class Prioritizado(models.Model):
	nombre = models.CharField(max_length=250)

	def __unicode__(self):
		return self.nombre

class Papel(models.Model):
	nombre = models.CharField(max_length=100)

	def __unicode__(self):
		return self.nombre

class Categoria(models.Model):
	nombre = models.CharField(max_length=100)

	def __unicode__(self):
		return self.nombre

class Categoria_Innovacion(models.Model):
	nombre = models.CharField(max_length=100)

	def __unicode__(self):
		return self.nombre

	class Meta:
		verbose_name = 'Categoria de Innovación'
		verbose_name_plural = 'Categorias de Innovación'

class Categoria_Conocimiento(models.Model):
	nombre = models.CharField(max_length=100)

	def __unicode__(self):
		return self.nombre

	class Meta:
		verbose_name = 'Categoria de Conocimiento'
		verbose_name_plural = 'Categorias de Conocimiento'

class Categoria_Fuente(models.Model):
	nombre = models.CharField(max_length=100)

	def __unicode__(self):
		return self.nombre

	class Meta:
		verbose_name = 'Categoria de Fuente'
		verbose_name_plural = 'Categorias de Fuente'

class Seleccion_7a(models.Model):
	nombre = models.CharField(max_length=100)

	def __unicode__(self):
		return self.nombre

	class Meta:
		verbose_name = 'Selección pregunta 7a'
		verbose_name_plural = 'Selecciones pregunta 7a'

class Seleccion_7b(models.Model):
	nombre = models.CharField(max_length=100)

	def __unicode__(self):
		return self.nombre

	class Meta:
		verbose_name = 'Selección pregunta 7b'
		verbose_name_plural = 'Selecciones pregunta 7b'


class Tipo_Estudio(models.Model):
	nombre = models.CharField(max_length=100)

	def __unicode__(self):
		return self.nombre

	class Meta:
		verbose_name = 'Tipo de estudio'
		verbose_name_plural = 'Tipos de estudios'
