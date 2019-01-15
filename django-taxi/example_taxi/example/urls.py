from django.urls import re_path

from .apis import TripView

app_name = 'example_taxi'

urlpatterns = [
    re_path('', TripView.as_view({'get': 'list'}), name='trip_list'),
]