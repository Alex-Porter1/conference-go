from django.urls import path

from .api_views import api_list_attendees, api_show_attendee

urlpatterns = [
    path(
        "conferences/<int:conference_id>/attendees/",
        api_list_attendees,
        name="api_list_attendees",
    ),
    path("attendees/<int:pk>/", api_show_attendee, name="api_show_attendee"),
]
