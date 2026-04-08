from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import ensure_csrf_cookie
from .models import Resource
import json

# Create your views here.

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

@ensure_csrf_cookie
def showAdminPage(request):
    resources = list(Resource.objects.values("id", "name", "category", "location", "desc", "avail"))
    return render(request, 'adminpage/adminpage.html', {"resources": resources})
