from django.template.context import RequestContext
from django.shortcuts import render_to_response


def index(request):    
    r ='asa'
    return render_to_response('guest/home.html', {'asa':r},
                              context_instance=RequestContext(request))