from django.db import models

class Event(models.Model):
	name = models.CharField(max_length=60)
	description = models.TextField()
	url_image = models.CharField(max_length=100)
	place = models.CharField(max_length=60)
	cupo_max = models.PositiveSmallIntegerField()
	cupo_disp = models.PositiveSmallIntegerField()
	date = models.DateTimeField()

	def save(self, *args, **kwargs):
		if self.id:
			event_id = int(self.id)
			cupo_max = int(self.cupo_max)
			cupo_disp =int(Event.objects.get(pk=event_id).cupo_disp)
			cupo = int(Event.objects.get(pk=event_id).cupo_max)
			cupos_ocupados = cupo - cupo_disp


			if cupo==cupo_max:
				super(Event,self).save(*args,**kwargs)

			else:
				if cupo > cupo_max:
					if cupos_ocupados > cupo_max:
						raise NameError('Accion-NO_VALIDA')
					
					self.cupo_disp = cupo_max - cupos_ocupados
					super(Event,self).save(*args,**kwargs)
				else:
					self.cupo_disp = cupo_max - cupos_ocupados
					super(Event,self).save(*args,**kwargs)


		else:
			self.cupo_disp=self.cupo_max
			super(Event,self).save(*args,**kwargs)

class Reservation(models.Model):
	asistentes = models.PositiveSmallIntegerField()
	event = models.ForeignKey(Event, related_name='reservations')

	def save(self, *args, **kwargs):
		if self.id:
			reservation_id = int(self.id)
			reservation = Reservation.objects.get(pk=reservation_id)
			asistentes_old = int(reservation.asistentes)
			asistentes = int(self.asistentes)
			cupo_disp = int(self.event.cupo_disp)

			if asistentes ==0:
				raise NameError('Accion-NO_VALIDA')


			if asistentes > asistentes_old:
				if (asistentes - asistentes_old)>cupo_disp:
					raise NameError('Accion-NO_VALIDA')
				cupo_disp -= asistentes - asistentes_old
				self.event.cupo_disp = cupo_disp
				self.event.save()
				super(Reservation, self).save(*args, **kwargs)
			else:
				cupo_disp += asistentes_old - asistentes
				self.event.cupo_disp=cupo_disp
				self.event.save()
				super(Reservation, self).save(*args, **kwargs)





			
		else:	
			asistentes = int(self.asistentes)		
			event = self.event
			cupo_disp = int(event.cupo_disp)
			if asistentes > cupo_disp or asistentes==0:
				raise NameError('Accion-NO_VALIDA')
			event.cupo_disp=cupo_disp-self.asistentes
			event.save()
			super(Reservation,self).save(*args, **kwargs)








