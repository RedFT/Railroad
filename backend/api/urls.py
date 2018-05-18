from django.conf.urls import url
#from .views import fare_types
import views
from .models import FareTypes
from .models import Passengers
from .models import Reservations
from .models import SeatsFree
from .models import Segments
from .models import Stations
from .models import StopsAt
from .models import Trains
from .models import Trips

urlpatterns = [
    url(r'^fare_types/$', views.fare_types_list),
    url(r'^fare_types/(?P<fare_id>[0-9]+)/$', views.fare_type_detail),

    url(r'^passengers/$', views.passengers_list),
    url(r'^passengers/(?P<passenger_id>[0-9]+)/$', views.passenger_detail),

    url(r'^reservations/$', views.reservations_list),
    # url(r'^reservations/(?P<fare_id>[0-9]+)/$', views.reservation_detail),
    #
    # url(r'^seats_free/$', views.seats_free_list),
    # url(r'^seats_free/(?P<fare_id>[0-9]+)/$', views.seats_free_detail),
    #
    # url(r'^segments/$', views.segments_list),
    # url(r'^segments/(?P<fare_id>[0-9]+)/$', views.segment_detail),
    #
    url(r'^stations/$', views.stations_list),
    url(r'^stations/(?P<station_id>[0-9]+)/$', views.station_detail),
    #
    # url(r'^stops_at/$', views.stops_at_list),
    # url(r'^stops_at/(?P<fare_id>[0-9]+)/$', views.stops_at_detail),
    #
    # url(r'^trains/$', views.trains_list),
    # url(r'^trains/(?P<fare_id>[0-9]+)/$', views.train_detail),
    #
    # url(r'^trips/$', views.trips_list),
    # url(r'^trips/(?P<fare_id>[0-9]+)/$', views.trip_detail),
]

