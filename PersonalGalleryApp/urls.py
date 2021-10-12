from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    url('^$',views.index,name='index'),
    url('^location$',views.filter_by_location,name='location'),
    # url(r'^welcome_user/(?P<type>.+)/$','welcome_user')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)