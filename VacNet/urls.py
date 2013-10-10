from django.conf.urls import patterns, include, url
from VacBox import views
from django.conf import settings

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns(''
    , url(r'^$', views.vacBox, name='vacBox')
    , url(r'^createcase/', views.createCase, name='createCase')
    , url(r'^admin/', include(admin.site.urls))
    , url(r'^accounts/', include('accounts.urls'))
    , url(r'^c/(?P<code>\w+)/$', views.editCase, name='editCase')
    , url(r'^e/(?P<code>\w+)/$', views.addPeople, name='addPeople')
)

#For Static media
if settings.DEBUG:
    urlpatterns += patterns('',
            (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
            (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
        )

urlpatterns += patterns(''
    , url(r'^.*/', views.notFound, name='notFound')
)

