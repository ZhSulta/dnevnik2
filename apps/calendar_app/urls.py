from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('calendar_app.views',
    url(r"main/(\d+)/$", "main", name = "main"),     
    url(r'month/(\d+)/(\d+)/(prev|next)/$', 'month', name = 'month'),
    url(r"month/(\d+)/(\d+)/$", "month", name = 'month'),
    url(r'month/$', 'month', name = 'a'), 
    (r"main/$", "main"),
    url(r"^day/(\d+)/(\d+)/(\d+)/$", "day", name = 'day'),
)


