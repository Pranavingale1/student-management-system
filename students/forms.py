from django import forms
from .models import student

class StudentForm(forms.ModelForm):
    class Meta:
        model = student
        fields = '__all__'
        labels = {
            'student_number':'Student number',
            'first_name':'First name',
            'last_name':'Last name',
            'email':'Email',
            'field_of_study':'Field of study',
            'CGPA':'CGPA',
        }
        
        widgets = {
            'student_number': forms.NumberInput(attrs={'class':'form-control'}),
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'field_of_study':forms.TextInput(attrs={'class':'form-control'}),
            'CGPA':forms.NumberInput(attrs={'class':'form-control'}),
        }