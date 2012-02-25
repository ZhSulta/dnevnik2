from accounts.forms import LoginForm, TeacherProfileForm, StudentProfileForm, ParentProfileForm
from django.template.context import RequestContext
from django.shortcuts import render_to_response
from apps.models.models import Temporary, Teacher, TeacherProfile,Student, StudentProfile, Parent, ParentProfile, Organization
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate,login as login_, logout as logout_
from django.contrib.auth.models import User
from django.utils.datetime_safe import datetime
from apps.models import settings as ns

def login(request):    
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username1  = request.POST['username']
            pwd1  = request.POST['password']             
            try:
                temp = Temporary.objects.get(username = username1,pwd = pwd1)
                return HttpResponseRedirect(reverse('temp', args = [username1,pwd1]))
            except Temporary.DoesNotExist:                                                        
                username = request.POST['username']
                password = request.POST['password']
                user = authenticate(username=username, password=password)
                if user is not None:
                    if user.is_active:
                        login_(request, user) 
                        try:
                            print user
                            teacher = Teacher.objects.get(user_id = user)                                                  
                            return HttpResponseRedirect(reverse('teacher_main_page'))
                        except Teacher.DoesNotExist:
                            try:
                                student = Student.objects.get(user_id = user)                       
                                return HttpResponseRedirect(reverse('student_main_page'))
                            except Student.DoesNotExist:
                                try:
                                    parent = Parent.objects.get(user_id = user)                       
                                    return HttpResponseRedirect(reverse('parent_main_page'))
                                except Parent.DoesNotExist:                                
                                    try:
                                        org = Organization.objects.get(user_id = user)                       
                                        return HttpResponseRedirect(reverse('organization_main_page'))
                                    except Organization.DoesNotExist:
                                        return HttpResponseRedirect(reverse('guest'))                            
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
    temp = Temporary.objects.get(username = u,pwd = p)    
    if request.method == 'POST':
        role = ''
        if temp.role == ns.TEACHER_POSITION:
            form = TeacherProfileForm(request.POST)
            role = 'teacher'
        elif temp.role == ns.STUDENT_POSITION:
            form = StudentProfileForm(request.POST)
            role = 'student'
        elif temp.role == ns.PARENTS_POSITION:
            form = ParentProfileForm(request.POST)        
            role = 'parent'
        if form.is_valid():
            dic = {
                'email':form.cleaned_data.get('email'),
                'username':form.cleaned_data.get('username'),
                'first_name':form.cleaned_data.get('first_name'),
                'last_name':form.cleaned_data.get('last_name'),             
                'is_active':True,
                }
            user = User(** dic)            
            if form.cleaned_data.get('password1'):
                user.set_password(form.cleaned_data.get('password1'))
            
            
            address = form.cleaned_data.get('address')
            mobile = form.cleaned_data.get('mobile')
            email = form.cleaned_data.get('email')
            #birth = form.cleaned_data.get('birth')            
            gender = form.cleaned_data.get('gender')
            nationality = form.cleaned_data.get('nationality')
                    
            if role == 'teacher':                    
                teacher = Teacher(user_id = user,school = temp.school)                
                teacherProfile = TeacherProfile(email=email,mobile=mobile,address=address,teacher=teacher,gender=gender,nationality=nationality)
                user.save()
                teacher.save()
                teacherProfile.save()
            elif role == 'parent':
                student = form.cleaned_data.get('student')
                user1 = User.objects.get(username = student)    
                student = Student.objects.get(user_id = user1)                                  
            
                parent = Parent(user = user,school = temp.school,child  = student,pk = user)
                print parent.user,parent.school,parent.child,parent.pk
                parentProfile = ParentProfile(email=email,mobile=mobile,address=address,parent=parent,gender=gender,nationality=nationality)                    
                parentProfile.save()
                parent.save()
                user.save()
                
            elif role == 'student':
                student = Student(user_id = user,school = temp.school)                
                studentProfile = StudentProfile(email=email,mobile=mobile,address=address,student=student,gender=gender,nationality=nationality)
                user.save()
                student.save()                
                studentProfile.save()
            
            temp.delete()
            
            return HttpResponseRedirect(reverse('login'))
    else:        
        if temp.role == ns.TEACHER_POSITION:
            form = TeacherProfileForm()         
        elif temp.role == ns.STUDENT_POSITION:
            form = StudentProfileForm()            
        elif temp.role == ns.PARENTS_POSITION:
            form = ParentProfileForm()                    
                    
    rc = RequestContext(request, { 'form':form,'u':u,'p':p})
    return render_to_response('registration/temp.html', rc)    

        