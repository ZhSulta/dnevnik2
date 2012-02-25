from django.template.context import RequestContext
from django.shortcuts import render_to_response

def index(request):
    rc = RequestContext(request, {})
    return render_to_response('teacher/home.html', rc)   
