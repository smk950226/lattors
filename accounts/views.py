from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import login as auth_login
from allauth.socialaccount.models import SocialApp
from allauth.socialaccount.templatetags.socialaccount import get_providers
from allauth.socialaccount.views import SignupView
from .forms import MentorForm, SignupForm

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(settings.LOGIN_URL)
    else:
        form = SignupForm()
    return render(request, 'accounts/signup_form.html', {
        'form': form,
        })

@login_required
def profile(request):
    return render(request, 'accounts/profile.html')

def login(request):
    providers = []
    for provider in get_providers():
        try:
            provider.social_app = SocialApp.objects.get(provider = provider.id, sites = settings.SITE_ID)
        except SocialApp.DoesNotExist:
            provider.social_app = None
        providers.append(provider)

    return auth_login(request,
        template_name = 'accounts/login_form.html',
        extra_context = {'providers' : providers})

@login_required
def admin_mentor(request):
    if request.method == 'POST':
        form = MentorForm(request.POST, request.FILES)
        if form.is_valid():
            mentor = form.save(commit=False)
            mentor.user = request.user
            mentor.save()
            return redirect('root')
    else:
        form = MentorForm()
    return render(request, 'accounts/admin_mentor_form.html', {
        'form': form,
    })

class MySignupView(SignupView):
    form_class = SignupForm
    template_name = 'accounts/socialsignup_form.html'


mysignup = MySignupView.as_view()