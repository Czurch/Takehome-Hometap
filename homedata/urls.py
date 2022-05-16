from opcode import hasjabs
from django.urls import path
from . import views
urlpatterns = [
    path('property/<address>/<int:zipcode>/sewer/<sewer_type>/', views.getSewer),
    path('property/<address>/<int:zipcode>/sewer/', views.getSewer),
    path('property/<address>/<int:zipcode>/', views.propertyData)
]