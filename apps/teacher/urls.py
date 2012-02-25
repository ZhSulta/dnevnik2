from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('teacher.views',
    url(r'^$', 'index',name = 'teacher_main_page'),    
)

