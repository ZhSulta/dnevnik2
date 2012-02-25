from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('org.views',
    url(r'^$', 'index', name = 'org'), 
    
    url(r'school_reg/$', 'school_reg', name = 'school_reg'),
    url(r'parents__temp_reg/$', 'parents_temp_reg', name = 'parents_temp_reg'),
    url(r'students_temp_reg/$', 'students_temp_reg', name = 'students_temp_reg'),
    url(r'teachers_temp_reg/$', 'teachers_temp_reg', name = 'teachers_temp_reg'),    
    
    url(r'schools_list/$', 'schools_list', name = 'schools_list'),
    url(r'school_info//(\d+)$', 'school_info', name = 'school_info'),
    url(r'school_del/(\d+)/$', 'school_del', name = 'school_del'),
    
    url(r'teachers_list/$', 'teachers_list', name = 'teachers_list'),
    url(r'teachers_info/(\d)/$', 'teachers_info', name = 'teachers_info'),
    url(r'teachers_del/(\d+)/$', 'teachers_del', name = 'teachers_del'),
    url(r'teachers_temp_del/(\d+)/$', 'teachers_temp_del', name = 'teachers_temp_del'),
    
    url(r'parents_list/$', 'parents_list', name = 'parents_list'),
    url(r'parents_info/$', 'parents_info', name = 'parents_info'),
    url(r'parents_del/(\d+)/$', 'parents_del', name = 'parents_del'),
    url(r'parents_temp_del/(\d+)/$', 'parents_temp_del', name = 'parents_temp_del'),
    
    url(r'students_list/$', 'students_list', name = 'students_list'),
    url(r'students_info/$', 'students_info', name = 'students_info'),
    url(r'students_del/(\d+)/$', 'students_del', name = 'students_del'),
    url(r'students_temp_del/(\d+)/$', 'students_temp_del', name = 'students_temp_del'),    
    
    url(r'city_add/$', 'city_add', name = 'city_add'),
    url(r'city_list/$', 'city_list', name = 'city_list'),
    url(r'city_del/(\d+)/$', 'city_del', name = 'city_del'),
)

