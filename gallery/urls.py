from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$', views.gallery_of_day, name='todaysGallery'),
    url('^$', views.search_results, name='search_results'),
    url(r'^location/(\d+)', views.filter_by_location, name='location')
]
