from django.conf.urls import url
from django.db.models.query_utils import PathInfo
from django.urls.conf import path
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    url('^$',views.index,name='index'),
    url('^search$',views.search_category,name='search_category'),
    #url(r'^location/(?P<location>\s)/$', views.filter_by_location, name='filter_by_location'),
    path(r'^location/<location>', views.filter_by_location, name='filter_by_location'),
    url(r'^image/(\d+)',views.singleimage , name='singleimage')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)