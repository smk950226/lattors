from django import forms
from .models import Mentor,MyUser
from django.contrib.auth.forms import UserCreationForm

class MentorForm(forms.ModelForm):
    class Meta:
        model = Mentor
        fields = ['name', 'tel', 'addr', 'school', 'major', 'sub_major', 'grade', 'photo', 'intro']


class SignupForm(UserCreationForm):
    username = forms.CharField(label = '이름')
    nickname = forms.CharField(label = '닉네임')
    email = forms.EmailField(label = 'E-mail')

    class Meta:
        model = MyUser
        fields = ['username', 'nickname', 'email']
        widget = {
            'username':forms.TextInput(attrs={'class': 'form-group',
                                'placeholder': '이름',
                                }),
            'nickname':forms.TextInput(attrs={'class': 'form-group',
                                'placeholder': '닉네임',
                                }),
            'email':forms.EmailInput(attrs={'class': 'form-group',
                            'placeholder': 'E-mail',
                            }),
        }