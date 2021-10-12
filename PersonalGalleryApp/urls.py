from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    url('^$',views.index,name='index'),
    url('^location/<str:value>/$',views.filter_by_location,name='location'),
    # url(r'^welcome_user/(?P<type>.+)/$','welcome_user')
    url('^search$',views.search_category,name='search_category'),

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)