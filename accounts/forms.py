from django import forms
from .models import Mentor,MyUser
from django.contrib.auth.forms import UserCreationForm
from allauth.socialaccount.forms import SignupForm as AllauthSignupForm

class MentorForm(forms.ModelForm):
    class Meta:
        model = Mentor
        fields = ['name', 'tel', 'addr', 'school', 'major', 'sub_major', 'grade', 'photo', 'intro']


class SignupForm(AllauthSignupForm):
    username = forms.CharField(label = '이름', widget = forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': '이름',
    }))
    nickname = forms.CharField(label = '닉네임', widget = forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': '닉네임',
    }))

    class Meta:
        model = MyUser
        fields = ['username', 'nickname']

    def signup(self, request, user):
        user.username = self.cleaned_data['username']
        user.nickname = self.cleaned_data['nickname']