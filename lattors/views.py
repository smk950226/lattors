from django.shortcuts import render, redirect, get_object_or_404
from .models import Mentors, Mentee, ActPhoto
from .forms import MentorsForm, MenteeForm, ActPhotoForm
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.db.models import F

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

talk_mentor = ListView.as_view