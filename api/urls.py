from django.conf.urls import url
from api import views

urlpatterns = [
	url(r'^events/$', views.event_list),
]