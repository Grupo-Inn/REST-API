from django.forms import widgets
from rest_framework import serializers
from api.models import Event, Reservation

class EventSerializer(serializers.ModelSerializer):
	cupo_disp = serializers.ReadOnlyField()
	class Meta:
		model = Event
		fields = ('id','name', 'description', 'url_image', 'place', 'cupo_max', 'cupo_disp', 'date',)

class ReservationSerializer(serializers.ModelSerializer):
	class Meta:
		model= Reservation
		fields=('id','asistentes','event',)

