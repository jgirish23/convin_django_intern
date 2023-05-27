from django.urls import path
from . import views
urlpatterns = [
    path("", views.Home),
    path("rest/v1/calendar/init/", views.GoogleCalendarInitView,name="google_authentication"),
    path("rest/v1/calendar/redirect/",views.GoogleCalendarRedirectView,name="list_calendar_events"),
]