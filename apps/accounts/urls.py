from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('accounts.views',
     url(r'login/$', 'login',name = 'login'),
     url(r'temp/(?P<u>\w+)/(?P<p>\w+)/$', 'temp',name = 'temp'),
#     url(r'^logout/$', 'logout', name='logout'),
                     
        
)

