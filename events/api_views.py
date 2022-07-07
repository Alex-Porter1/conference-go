from django.http import JsonResponse
from common.json import ModelEncoder
from .models import Conference, Location

class LocationListEncoder(ModelEncoder):
    model = Location
    properties = ["name",]

class LocationDetailEncoder(ModelEncoder):
    model = Location
    properties = [
        "name",
        "city",
        "room_count",
        "created",
        "updated",
    ]

    def get_extra_data(self, o):
        return { "state": o.state.abbreviation }


class ConferenceDetailEncoder(ModelEncoder):
    model = Conference
    properties = [
        "name",
        "description",
        "max_presentations",
        "max_attendees",
        "starts",
        "ends",
        "created",
        "updated",
        "location",
    ]
    encoders = {
        "location": LocationListEncoder(),
    }

class ConferenceListEncoder(ModelEncoder):
    model = Conference
    properties = ["name"]

def api_list_conferences(request):
    """
    Lists the conference names and the link to the conference.

    Returns a dictionary with a single key "conferences" which
    is a list of conference names and URLS. Each entry in the list
    is a dictionary that contains the name of the conference and
    the link to the conference's information.

    {
        "conferences": [
            {
                "name": conference's name,
                "href": URL to the conference,
            },
            ...
        ]
    }
    """
def api_list_conferences(request):
    conferences = Conference.objects.all()
    return JsonResponse(
        {"conferences": conferences},
        encoder=ConferenceListEncoder,
    )


def api_show_conference(request, pk):
    """
    Returns the details for the Conference model specified
    by the pk parameter.

    This should return a dictionary with the name, starts,
    ends, description, created, updated, max_presentations,
    max_attendees, and a dictionary for the location containing
    its name and href.

    {
        "name": the conference's name,
        "starts": the date/time when the conference starts,
        "ends": the date/time when the conference ends,
        "description": the description of the conference,
        "created": the date/time when the record was created,
        "updated": the date/time when the record was updated,
        "max_presentations": the maximum number of presentations,
        "max_attendees": the maximum number of attendees,
        "location": {
            "name": the name of the location,
            "href": the URL for the location,
        }
    }
    """
    conference = Conference.objects.get(id=pk)
    return JsonResponse(
        conference,
        encoder=ConferenceDetailEncoder,
        safe=False
    )


def api_list_locations(request):
    """
    Lists the location names and the link to the location.

    Returns a dictionary with a single key "locations" which
    is a list of location names and URLS. Each entry in the list
    is a dictionary that contains the name of the location and
    the link to the location's information.
    """

    locations = Location.objects.all()
    return JsonResponse(
        {"locations": locations},
        encoder=LocationListEncoder,
    )


def api_show_location(request, pk):
    location = Location.objects.get(id=pk)
    return JsonResponse(
        location,
        encoder=LocationDetailEncoder,
        safe=False,
    )
