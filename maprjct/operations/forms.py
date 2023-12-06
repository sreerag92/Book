from django import forms
from operations.models import book,Student,std1

class demo(forms.Form):
    Name = forms.CharField()
    Email = forms.EmailField()

class Bookform(forms.ModelForm):
    class Meta:
        model=book
        fields = '__all__'


class Studform(forms.ModelForm):
    class Meta:
        model=Student
        fields = '__all__'

class std1form(forms.ModelForm):
    class Meta:
        model=std1
        fields = '__all__'
        