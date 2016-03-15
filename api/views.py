from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models import Event
from api.serializers import EventSerializer

@api_view(['GET','POST'])

def event_list(request):
	"""
		Proporciona todas los eventos
	"""

	if request.method=='GET':
		events = Event.objects.all()
		serializer = EventSerializer(events, many=True)
		return Response(serializer.data)

	elif request.method== 'POST':
		serializer = EventSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

		
