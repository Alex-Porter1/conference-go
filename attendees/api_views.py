from django.http import JsonResponse

from .models import Attendee


def api_list_attendees(request, conference_id):
    """
    Lists the attendees names and the link to the attendee
    for the specified conference id.

    Returns a dictionary with a single key "attendees" which
    is a list of attendee names and URLS. Each entry in the list
    is a dictionary that contains the name of the attendee and
    the link to the attendee's information.
    """

    response = []
    attendees = Attendee.objects.all()
    for attendee in attendees:
        response.append(
    {
        "attendees": [
            {
                "name": attendee.name,
                "href": attendee.get_api_url(),
            }
        ]
    }
        )
    return JsonResponse({"attendees": response})


def api_show_attendee(request, pk):
    """
    Returns the details for the Attendee model specified
    by the pk parameter.

    This should return a dictionary with email, name,
    company name, created, and conference properties for
    the specified Attendee instance.
    """
    attendees = Attendee.objects.get(id=pk)
    return JsonResponse(
    {
        "email": attendees.email,
        "name": attendees.name,
        "company_name": attendees.company_name,
        "created": attendees.created,
        "conference": {
            "name": attendees.conference.name,
            "href": attendees.conference.get_api_url(),
        },
    }
    
    )
