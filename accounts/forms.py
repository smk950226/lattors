from django import forms
from .models import Mentor,Profile
from django.contrib.auth.forms import UserCreationForm
from allauth.socialaccount.forms import SignupForm as AllauthSignupForm
from allauth.socialaccount.adapter import get_adapter

class MentorForm(forms.ModelForm):
    class Meta:
        model = Mentor
        fields = ['tel', 'addr', 'school', 'major', 'sub_major', 'grade', 'photo', 'intro']
        widgets = {
            'tel': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '전화번호',
            }),
            'addr': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '주소',
                'size': '100'
            }),
            'school': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '학교',
            }),
            'major': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '전공',
            }),
            'sub_major': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '복수/부 전공',
            }),
            'grade': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': '학년',
            }),
            'photo': forms.FileInput(attrs={
                'value': '프로필 사진'
            }),
            'intro': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': '자기소개',
                'rows': '10',
                'cols': '150'
            })
        }


class SignupForm(AllauthSignupForm):
    username = forms.CharField(label = '닉네임', widget = forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': '닉네임',
    }))
    name = forms.CharField(label = '이름', widget = forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': '이름',
    }))
    email = forms.EmailField(label = 'E-mail', required=True, widget = forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'E-mail',
    }))

    class Meta:
        fields = ['username', 'nickname', 'email']

    def signup(self, request, user):
        user.username = self.cleaned_data['username']
        user.nickname = self.cleaned_data['nickname']
        user.email = self.cleaned_data['email']
    
    def save(self,request):
        adapter = get_adapter(request)
        user = adapter.save_user(request, self.sociallogin, form=self)

        profile = Profile.objects.create(
            user = user,
            name = self.cleaned_data['name'],
            nickname = self.cleaned_data['username'],
            emailaddress = self.cleaned_data['email'],
        )

        return user