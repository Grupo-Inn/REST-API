from django.conf.urls import url
from api import views

urlpatterns = [
	url(r'^events/$', views.EventList.as_view()),
	url(r'^events/(?P<pk>[0-9]+)$', views.EventDetail.as_view()),
	url(r'^events/(?P<pk>[0-9]+)/reservations$', views.EventReservationsList.as_view()),
	url(r'^reservations/(?P<pk>[0-9]+)$', views.ReservationDetail.as_view()),
]