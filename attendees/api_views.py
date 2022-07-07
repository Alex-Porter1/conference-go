from django.http import JsonResponse
from common.json import ModelEncoder
from .models import Attendee

class AttendeeListEncoder(ModelEncoder):
    model = Attendee
    properties = ["name",]

class AttendeeDetailEncoder(ModelEncoder):
    model = Attendee
    properties = [
        "email",
        "name",
        "company_name",
        "created",
        "conference"
    ]

    def get_extra_data(self, o):
        return { "conference": o.conference.name }



def api_list_attendees(request, conference_id):
    """
    Lists the attendees names and the link to the attendee
    for the specified conference id.

    Returns a dictionary with a single key "attendees" which
    is a list of attendee names and URLS. Each entry in the list
    is a dictionary that contains the name of the attendee and
    the link to the attendee's information.
    """

    attendees = Attendee.objects.all()
    return JsonResponse(
        {"attendees": attendees},
        encoder=AttendeeListEncoder,
    )


def api_show_attendee(request, pk):
    """
    Returns the details for the Attendee model specified
    by the pk parameter.

    This should return a dictionary with email, name,
    company name, created, and conference properties for
    the specified Attendee instance.
    """
    attendee = Attendee.objects.get(id=pk)
    return JsonResponse(
        attendee,
        encoder=AttendeeDetailEncoder,
        safe=False
    )
