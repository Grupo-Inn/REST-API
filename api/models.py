from django.db import models

class Event(models.Model):
	nombre = models.CharField(max_length=60)
	descripcion = models.TextField()
	url_image = models.CharField(max_length=100)
	tipo = models.CharField(max_length=20)
	lugar = models.CharField(max_length=60)
	cupo_max = models.PositiveSmallIntegerField()
	fecha = models.DateTimeField()