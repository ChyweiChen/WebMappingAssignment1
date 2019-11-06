from django.shortcuts import render
from django.views import generic
from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance
from .models import Substation

longitude = -53.350403
latitude = 6.264477

user_location = Point(longitude, latitude, srid=4326)


class Home(generic.ListView):
    model = Substation
    context_object_name = 'nearsubway'
    queryset = Substation.objects.annotate(distance=Distance('location',
                                                             user_location)/100000
                                           ).order_by('distance')[0:6]
    template_name = 'Subway/index.html'
