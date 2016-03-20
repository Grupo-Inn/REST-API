from rest_framework import status
from rest_framework import mixins
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from api.models import Event, Reservation
from api.serializers import EventSerializer, ReservationSerializer


class EventList(generics.ListCreateAPIView):
	"""
		Proporciona todas los eventos
	"""
	queryset = Event.objects.all()
	serializer_class = EventSerializer

class EventDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Event.objects.all()
	serializer_class = EventSerializer


class EventReservationsList(APIView):

	def get(self, request, pk):
		event = Event.objects.get(pk=pk)
		reservations = event.reservations
		serializer = ReservationSerializer(reservations, many=True)
		return Response(serializer.data)

	def post(self, request, pk):
		request.data['event']=pk
		serializer=ReservationSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)	

class ReservationDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Reservation.objects.all()
	serializer_class = ReservationSerializer
