from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import ensure_csrf_cookie
from django.utils.dateparse import parse_datetime
from .models import Resource, Reservation
import json

# Create your views here.


# Called when a resource is added, creates a Resource object
@require_POST
def add_resource(request):
    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({"success": False, "error": "Invalid JSON"}, status=400)

    name = data.get("name", "").strip()
    location = data.get("location", "").strip()
    category = data.get("category", "").strip()
    desc = data.get("desc", "").strip()
    avail = data.get("avail", "").strip()

    if not name or not location or not desc:
        return JsonResponse({"success": False, "error": "Missing required fields"}, status=400)
    resource = Resource.objects.create(
        name = data["name"],
        location = data["location"],
        category = data["category"],
        desc = data["desc"],
        avail = data["avail"],
    )
    return JsonResponse({
        "success": True,
        "resource": {
            "id": resource.id,
            "name": resource.name,
            "location": resource.location,
            "category": resource.category,
            "desc": resource.desc,
            "avail": resource.avail,
        }
    })


# Called when a resource is deleted, gets rid of a Resource object
@require_POST
def remove_resource(request):
    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({"success": False, "error": "Invalid JSON"}, status=400)

    resource_id = data.get("id", "")

    if not resource_id:
        return JsonResponse({"success": False, "error": "Missing required fields"}, status=400)

    Resource.objects.filter(id=resource_id).delete()

    return JsonResponse({
        "success": True
    })

@require_POST
def add_reservation(request):
    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({"success": False, "error": "Invalid JSON"}, status=400)

    resource_id = data.get("resource_id", "")
    timeSlot = data.get("timeSlot", "").strip()
    timeReserved = data.get("timeReserved", "").strip()

    if not resource_id or not timeSlot or not timeReserved:
        return JsonResponse({"success": False, "error": "Missing required fields"}, status=400)

    try:
        resource = Resource.objects.get(id=resource_id)
    except Resource.DoesNotExist:
        return JsonResponse({"success": False, "error": "Resource not found"}, status=404)

    parsed_time = parse_datetime(timeReserved)
    if parsed_time is None:
        return JsonResponse({"success": False, "error": "Invalid reservation time"}, status=400)

    reservation = Reservation.objects.create(
        resource = resource,
        timeSlot = timeSlot,
        timeReserved = parsed_time,
    )
    return JsonResponse({
        "success": True,
        "reservation": {
            "id": reservation.id,
            "resource": {
                "id": resource.id,
                "name": resource.name,
                "location": resource.location,
                "category": resource.category,
            },
            "timeSlot": reservation.timeSlot,
            "timeReserved": reservation.timeReserved.isoformat(),
        }
    })

@require_POST
def remove_reservation(request):
    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({"success": False, "error": "Invalid JSON"}, status=400)

    reservation_id = data.get("reservation_id", "")

    if not reservation_id:
        return JsonResponse({"success": False, "error": "Missing required fields"}, status=400)

    Reservation.objects.filter(id=reservation_id).delete()

    return JsonResponse({
        "success": True
    })

# Used by template to access Resource objects
def get_resources(request):
    resources = list(Resource.objects.values("id", "name", "category", "location", "desc", "avail"))
    return JsonResponse({"resources": resources})

def get_reservations(request):
    reservations = []

    for reservation in Reservation.objects.select_related("resource").all():
        reservations.append({
            "id": reservation.id,
            "resource": {
                "id": reservation.resource.id,
                "name": reservation.resource.name,
                "location": reservation.resource.location,
                "category": reservation.resource.category,
            },
            "timeSlot": reservation.timeSlot,
            "timeReserved": str(reservation.timeReserved),
        })

    return JsonResponse({"reservations": reservations})

# Renders html file
@ensure_csrf_cookie
def showAdminPage(request):
    return render(request, 'adminpage/adminpage.html')