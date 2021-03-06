from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns=[
    url(r'^$', views.photos, name='photos'),
    url(r'search/', views.search_results, name='search_results'),
    url(r'location/(?P<location_name>\w+)/>\)/$', views.get_image_by_location, name='location'),
]



if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)