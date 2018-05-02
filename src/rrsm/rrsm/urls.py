from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include
from django.contrib import admin
from django.views.generic import RedirectView
from django.urls import path, re_path
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth import views as auth_views
from django.views.decorators.cache import cache_page
from rrsmi import views as rrsmi_view

CACHE_TIME_SHORT = int(getattr(settings, "CACHE_TIME_SHORT", 0))
CACHE_TIME_MEDIUM = int(getattr(settings, "CACHE_TIME_MEDIUM", 0))
CACHE_TIME_LONG = int(getattr(settings, "CACHE_TIME_LONG", 0))

urlpatterns = [
    path('', cache_page(CACHE_TIME_MEDIUM)(rrsmi_view.HomeListView.as_view()),name='home'),
    re_path(r'^recent/(?P<days>\w+)/$',
        cache_page(CACHE_TIME_MEDIUM)(rrsmi_view.RecentEventsListView.as_view()), name='recent_events'),
    re_path(r'^event/(?P<event_public_id>\w+)/$',
        cache_page(CACHE_TIME_LONG)(rrsmi_view.EventDetailsListView.as_view()), name='event_details'),
    re_path(r'^event/(?P<event_public_id>\w+)/(?P<network_code>\w+)/(?P<station_code>\w+)/$',
        cache_page(CACHE_TIME_LONG)(rrsmi_view.StationStreamsListView.as_view()), name='station_streams'),
    path('search_events/', rrsmi_view.search_events, name='search_events'),
    path('admin/', admin.site.urls),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Add custom handlers for the HTTP error codes
handler404 = 'rrsmi.views.custom_404'
handler500 = 'rrsmi.views.custom_500'
