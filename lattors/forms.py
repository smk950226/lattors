from django import forms
from .models import Mentors, Mentee

class MentorsForm(forms.ModelForm):
    class Meta:
        model = Mentors
        fields = ['name', 'tel', 'addr', 'school', 'major', 'sub_major', 'grade', 'photo', 'intro']


class MenteeForm(forms.ModelForm):
    class Meta:
        model= Mentee
        fields = ['name', 'tel', 'addr', 'school', 'school_type', 'grade', 'school_expect', 'major_expect', 'photo', 'intro']
        