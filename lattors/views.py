from django.shortcuts import render, redirect, get_object_or_404
from .models import Mentors, Mentee, ActPhoto, TalkMentor
from .forms import MentorsForm, MenteeForm, ActPhotoForm, TalkMentorForm
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DeleteView
from django.db.models import F
from accounts.models import Profile
from django.urls import reverse_lazy

def main(request):
    mentor1 = Mentors.objects.all().order_by('-hits')[:2][0]
    mentor2 = Mentors.objects.all().order_by('-hits')[:2][1]
    photos = ActPhoto.objects.all().order_by('?')[:8]
    return render(request, 'lattors/main.html', {
        'mentor1': mentor1,
        'mentor2': mentor2,
        'photos': photos
    })

@login_required
def admin_mentor(request):
    if request.method == 'POST':
        form = MentorsForm(request.POST, request.FILES)
        if form.is_valid():
            mentor = form.save(commit=False)
            mentor.user = request.user
            mentor.save()
            return redirect('root')
    else:
        form = MentorsForm()
    return render(request, 'lattors/admin_mentor_form.html', {
        'form': form,
    })

@login_required
def admin_mentee(request):
    if request.method == 'POST':
        form = MenteeForm(request.POST, request.FILES)
        if form.is_valid():
            mentee = form.save(commit=False)
            mentee.user = request.user
            mentee.save()
            form.save_m2m()
            return redirect('root')
    else:
        form = MenteeForm()
    return render(request, 'lattors/admin_mentee_form.html', {
        'form': form,
    })

def intro(request):
    return render(request, 'lattors/comp_intro.html')

def vision(request):
    return render(request, 'lattors/comp_vision.html')

def member(request):
    return render(request, 'lattors/comp_member.html')

def contact(request):
    return render(request, 'lattors/comp_contact.html')

mentors_list = ListView.as_view(model=Mentors, paginate_by=10)

def mentor_detail(request, id):
    Mentors.objects.filter(id=id).update(hits=F('hits')+1)
    mentor = get_object_or_404(Mentors, id=id)
    return render(request, 'lattors/mentor_detail.html', {
        'mentor': mentor,
    })

def act_list(request):
    return render(request, 'lattors/act_list.html')

def act_lattors(request):
    return render(request, 'lattors/act_lattors.html', {
        'mentors': Mentors.objects.all().order_by('-id')[:3],
    })

def act_comma(request):
    photos = ActPhoto.objects.all().order_by('?')[:6]
    return render(request, 'lattors/act_comma.html', {
        'photos': photos
    })

def act_photo(request):
    photos = ActPhoto.objects.all()
    return render(request, 'lattors/act_photo.html', {
        'photos': photos,
    })

def act_photo_add(request):
    if request.method == 'POST':
        form = ActPhotoForm(request.POST, request.FILES)
        if form.is_valid():
            mentor = form.save()
            return redirect('lattors:act_photo')
    else:
        form = ActPhotoForm()
    return render(request, 'lattors/act_photo_add.html', {
        'form': form,
    })

talk_mentor = ListView.as_view(model=TalkMentor, paginate_by=20)

@login_required
def talk_mentor_new(request):
    if request.method == 'POST':
        form = TalkMentorForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.writer = request.user.profile
            article.nickname = request.user.profile.nickname
            article.save()
            return redirect(article)
    else:
        form = TalkMentorForm()
    return render(request, 'lattors/talkmentor_form.html', {
        'form': form,
    })

def talk_mentor_detail(request, id):
    TalkMentor.objects.filter(id=id).update(hits=F('hits')+1)
    article = get_object_or_404(TalkMentor, id=id)
    next_article = TalkMentor.objects.filter(id__gt=article.id).order_by('id').first()
    previous_article = TalkMentor.objects.filter(id__lt=article.id).order_by('-id').first()
    
    return render(request, 'lattors/talkmentor_detail.html', {
        'article': article,
        'next_article': next_article,
        'previous_article': previous_article,
    })

def talk_mentor_edit(request, id):
    article = get_object_or_404(TalkMentor, id=id)
    if request.method == 'POST':
        form = TalkMentorForm(request.POST, instance = article)
        if form.is_valid():
            article = form.save(commit=False)
            article.writer = request.user.profile
            article.nickname = request.user.profile.nickname
            article.save()
            return redirect(article)
    else:
        form = TalkMentorForm(instance = article)

    return render(request, 'lattors/talkmentor_edit.html', {
        'form': form,
    })

talk_mentor_delete = DeleteView.as_view(model = TalkMentor, success_url=reverse_lazy('lattors:talk_mentor'), pk_url_kwarg='id')