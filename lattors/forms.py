from django import forms
from .models import Mentors, Mentee, ActPhoto, TalkMentor, TalkMentee

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


class TalkMentorForm(forms.ModelForm):
    class Meta:
        model = TalkMentor
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '제목',
                'size': '120',
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': '내용',
                'rows': '10',
                'cols': '200',
            })
        }


class TalkMenteeForm(forms.ModelForm):
    class Meta:
        model = TalkMentee
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '제목',
                'size': '120',
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': '내용',
                'rows': '10',
                'cols': '200',
            })
        }