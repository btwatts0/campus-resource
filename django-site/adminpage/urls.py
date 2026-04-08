from django.urls import path
from . import views

urlpatterns = [
    # pages
    path('', views.showAdminPage),

    # API
    path('add-resource/', views.add_resource, name='add_resource')
]
