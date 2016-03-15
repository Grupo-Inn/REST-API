from django.forms import widgets
from rest_framework import serializers
from api.models import Event

class EventSerializer(serializers.ModelSerializer):
	class Meta:
		model = Event
		fields = ('id','nombre', 'descripcion', 'url_image', 'lugar', 'cupo_max', 'fecha',)
