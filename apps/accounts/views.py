from accounts.forms import LoginForm, TeacherProfileForm
from django.template.context import RequestContext
from django.shortcuts import render_to_response
from apps.models.models import Temporary, Teacher, TeacherProfile
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate,login as login_, logout as logout_
from django.contrib.auth.models import User


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username1  = request.POST['username']
            pwd1  = request.POST['password'] 
            print username1
            print pwd1    
            temp = Temporary.objects.get(username = username1,pwd = pwd1)
            if temp:
                return HttpResponseRedirect(reverse('temp'))
            else:
                username = request.POST['username']
                password = request.POST['password']
                user = authenticate(username=username, password=password)
                if user is not None:
                    if user.is_active:
                        login_(request, user)                        
                    else:
                        return reverse('guest')
                else:
                    return reverse('guest')
    else:
        form = LoginForm()
    rc = RequestContext(request, {'form':form, 'title':'Registration Form'})
    return render_to_response('registration/login.html', rc,
                              context_instance=RequestContext(request))     

def logout(request):
    logout_(request)
    return HttpResponseRedirect(reverse('guest'))

def temp(request,u,p):
    if request.method == 'POST':
        form = TeacherProfileForm(request.POST)
        if form.is_valid():
            dic = {
                'email':form.cleaned_data.get('email'),
                'username':form.cleaned_data.get('username'),
                'first_name':form.cleaned_data.get('first_name'),
                'last_name':form.cleaned_data.get('last_name'),             
                'is_active':True,
                }
            user = User(** dic)            
            user.set_password(form.cleaned_data.get('password1'))
            user.save()
            
            

#    teacher = models.OneToOneField(Teacher)

            address = form.cleaned_data.get('address')
            mobile = form.cleaned_data.get('mobile')
            email = form.cleaned_data.get('email')
            birth = form.cleaned_data.get('birth')
            gender = form.cleaned_data.get('gender')
            nationality = form.cleaned_data.get('nationality')
            
            
            teacher = Teacher(user_id = user)
            teacherProfile = TeacherProfile()
            
           
            if form.cleaned_data.get('password1'):
                user1.set_password(form.cleaned_data.get('password1'))
            form.save()
            user1.save()
            client.save()
            next = request.REQUEST.get('next', '/')
            return HttpResponseRedirect(next)
    else:
        form = TeacherProfileForm()
    rc = RequestContext(request, { 'form':form})

    return render_to_response('registration/temp.html', rc)    

        