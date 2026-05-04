from django.urls import path
from . import views

urlpatterns = [
    # pages
    path('', views.showAdminPage),

    # API (template needs to use these to access views functions)
    path('add-resource/', views.add_resource, name='add_resource'),
    path('remove-resource/', views.remove_resource, name='remove_resource'),
    path('get-resources/', views.get_resources, name="get_resources"),
    path('add-reservation/', views.add_reservation, name="add_reservation"),
    path('remove-reservation/', views.remove_reservation, name="remove_reservation"),
    path('get-reservations/', views.get_reservations, name="get_reservations"),
]
