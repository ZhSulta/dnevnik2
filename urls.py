from django.conf.urls.defaults import patterns, include, url
import settings

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',    
    url(r'^', include('guest.urls')),        
    url(r'^student/', include('student.urls')), 
    url(r'^teacher/', include('teacher.urls')),
    url(r'^parents/', include('parents.urls')),
    url(r'^school/', include('school.urls')),
    url(r'^org/',include('org.urls')),                               
    (r'^accounts/', include('accounts.urls')),
    (r'^accounts/', include('registration.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^calendar/', include('calendar_app.urls')),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', { 'document_root' : settings.MEDIA_ROOT }),
)
