from django.conf.urls import patterns, include, url
from VacBox import views
from django.conf import settings

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns(''
    , url(r'^$', views.vacBox, name='vacBox')
    , url(r'^admin/', include(admin.site.urls))
    , url(r'^accounts/', include('userena.urls')),
)

#For Static media
if settings.DEBUG:
    urlpatterns += patterns('',
            (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
            (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
        )

##Any override for userena views goes here:
#urlpatterns += patterns('',
#    url(r'^accounts/', include('django-registration.urls')),
#)
