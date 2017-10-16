from django import forms
from .models import Mentors, Mentee, ActPhoto

class MentorsForm(forms.ModelForm):
    class Meta:
        model = Mentors
        fields = ['name', 'tel', 'addr', 'school', 'major', 'sub_major', 'grade', 'photo', 'intro']


class MenteeForm(forms.ModelForm):
    class Meta:
        model= Mentee
        fields = ['name', 'tel', 'addr', 'school', 'school_type', 'grade', 'school_expect', 'major_expect', 'photo', 'intro']


class ActPhotoForm(forms.ModelForm):
    class Meta:
        model = ActPhoto
        fields = '__all__'
        widgets = {
            'photo': forms.FileInput(attrs={
                'value': '이미지',
            }),
            'year': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': '활동연도',
            }),
            'date': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '2017.01.01',
            }),
            'site': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '활동장소'
            }),
        }
        