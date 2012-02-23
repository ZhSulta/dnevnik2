from django import forms
from django.contrib.auth.models import User
from apps.models.models import School, City,TeacherProfile
from django.forms.fields import ChoiceField
from django.forms.widgets import RadioSelect

class LoginForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(max_length=20,widget=forms.PasswordInput(attrs={'minlength':'6'}))



GENDER_CHOICES = (('m', 'Male'), ('f', 'Female'))

class TeacherProfileForm(forms.ModelForm):
#            email = models.EmailField(max_length = 40,blank = True,)
#    mobile =  models.CharField(max_length = 255, blank = True, null = True)
#    address = models.CharField(max_length = 255, blank = True, null = True)    
#    teacher = models.OneToOneField(Teacher)
#    birth = models.DateField()
#    gender =  models.CharField(max_length = 255, blank = True, null = True)
#    nationality = models.CharField(max_length = 255, blank = True, null = True)
        
        
        
        
    first_name = forms.CharField(label = 'First Name:', max_length = 30, required = False)
    last_name = forms.CharField(label = 'Last name:', max_length = 30, required = False)
    password1 = forms.CharField(label = 'New password', widget = forms.PasswordInput, required = False)
    password2 = forms.CharField(label = "Confirm new password:", widget = forms.PasswordInput, required = False)

    class Meta:
        model = TeacherProfile
        fields = ('first_name', 'last_name', 'address', 'email' , 'birth' ,'gender','nationality','mobile', 'password1', 'password2')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1", "")
        password2 = self.cleaned_data["password2"]
        if password1 != password2:            
            raise forms.ValidationError('Incorrect confirmation password.')                
        return password2

    def clean_email(self):
        """
        Validate that the supplied email address is unique for the
        site.
        
        """        
        if User.objects.filter(email__iexact=self.cleaned_data['email']):
            raise forms.ValidationError('This e-mail is already used.')               
        return self.cleaned_data['email']


