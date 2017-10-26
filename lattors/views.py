from django.shortcuts import render, redirect, get_object_or_404
from .models import Mentors, Mentee, ActPhoto, TalkMentor, TalkMentee
from .forms import MentorsForm, MenteeForm, ActPhotoForm, TalkMentorForm, TalkMenteeForm
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DeleteView
from django.db.models import F, Q
from accounts.models import Profile
from django.urls import reverse_lazy
from accounts.models import Mentor
from django.views.generic.list import MultipleObjectMixin

class MentorSearchListView(ListView):
    def get_queryset(self):
        obj_list = self.model.objects.all()
        q = self.request.GET.get('q','')

        if q:
            obj_list = self.model.objects.filter(Q(name__icontains=q)|Q(major__icontains=q)|Q(sub_major__icontains=q)|Q(intro__icontains=q))

        return obj_list
    
    def get_context_data(self, **kwargs):
        """
        Get the context for this view.
        """
        queryset = kwargs.pop('object_list', self.object_list)
        page_size = self.get_paginate_by(queryset)
        context_object_name = self.get_context_object_name(queryset)
        if page_size:
            paginator, page, queryset, is_paginated = self.paginate_queryset(queryset, page_size)
            context = {
                'q': self.request.GET.get('q',''),
                'paginator': paginator,
                'page_obj': page,
                'is_paginated': is_paginated,
                'object_list': queryset
            }
        else:
            context = {
                'q': self.request.GET.get('q',''),
                'paginator': None,
                'page_obj': None,
                'is_paginated': False,
                'object_list': queryset
            }
        if context_object_name is not None:
            context[context_object_name] = queryset
        context.update(kwargs)
        return super(MultipleObjectMixin, self).get_context_data(**context)


class SearchListView(ListView):
    def get_queryset(self):
        obj_list = self.model.objects.all()
        q = self.request.GET.get('q','')

        if q:
            obj_list = self.model.objects.filter(Q(nickname__icontains=q)|Q(title__icontains=q)|Q(content__icontains=q))

        return obj_list
    
    def get_context_data(self, **kwargs):
        """
        Get the context for this view.
        """
        queryset = kwargs.pop('object_list', self.object_list)
        page_size = self.get_paginate_by(queryset)
        context_object_name = self.get_context_object_name(queryset)
        if page_size:
            paginator, page, queryset, is_paginated = self.paginate_queryset(queryset, page_size)
            context = {
                'q': self.request.GET.get('q',''),
                'paginator': paginator,
                'page_obj': page,
                'is_paginated': is_paginated,
                'object_list': queryset
            }
        else:
            context = {
                'q': self.request.GET.get('q',''),
                'paginator': None,
                'page_obj': None,
                'is_paginated': False,
                'object_list': queryset
            }
        if context_object_name is not None:
            context[context_object_name] = queryset
        context.update(kwargs)
        return super(MultipleObjectMixin, self).get_context_data(**context)



def main(request):
    mentor1 = Mentor.objects.all().order_by('-hits')[:2][0]
    mentor2 = Mentor.objects.all().order_by('-hits')[:2][1]
    newmentor1 = Mentor.objects.all().order_by('-id')[:2][0]
    newmentor2 = Mentor.objects.all().order_by('-id')[:2][1]
    photos = ActPhoto.objects.all().order_by('?')[:8]
    return render(request, 'lattors/main.html', {
        'mentor1': mentor1,
        'mentor2': mentor2,
        'newmentor1': newmentor1,
        'newmentor2': newmentor2,
        'photos': photos,
    })

@login_required
def admin_mentor(request):
    return redirect('admin_mentor')

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

mentors_list = MentorSearchListView.as_view(model=Mentor, paginate_by=10)

def mentor_detail(request, id):
    Mentor.objects.filter(id=id).update(hits=F('hits')+1)
    mentor = get_object_or_404(Mentor, id=id)
    return render(request, 'lattors/mentor_detail.html', {
        'mentor': mentor,
    })

def act_list(request):
    return render(request, 'lattors/act_list.html')

def act_lattors(request):
    return render(request, 'lattors/act_lattors.html', {
        'mentors': Mentor.objects.all().order_by('-id')[:3],
    })

def act_comma(request):
    photos = ActPhoto.objects.all().order_by('?')[:8]
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

talk_mentor = SearchListView.as_view(model=TalkMentor, paginate_by=20)

@login_required
def talk_mentor_new(request):
    if request.user.profile.adminmentor == False:
        if request.user.is_superuser:
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
        else:
            return redirect('lattors:talk_mentor_reject')

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

@login_required
def talk_mentor_edit(request, id):
    article = get_object_or_404(TalkMentor, id=id)

    if request.user.profile.adminmentor == False:
        if request.user.is_superuser:
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
        else:
            return redirect('lattors:talk_mentor_reject')

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

def talk_mentor_reject(request):
    return render(request, 'lattors/talkmentor_reject.html')

talk_mentor_delete = DeleteView.as_view(model = TalkMentor, success_url=reverse_lazy('lattors:talk_mentor'), pk_url_kwarg='id')

talk_mentee = SearchListView.as_view(model = TalkMentee, paginate_by = 20)

@login_required
def talk_mentee_new(request):
    if request.user.profile.adminmentor == True:
        if request.user.is_superuser:
            if request.method == 'POST':
                form = TalkMenteeForm(request.POST)
                if form.is_valid():
                    article = form.save(commit=False)
                    article.writer = request.user.profile
                    article.nickname = request.user.profile.nickname
                    article.save()
                    return redirect(article)
            else:
                form = TalkMenteeForm()
            return render(request, 'lattors/talkmentee_form.html', {
                'form': form,
            })
        else:
            return redirect('lattors:talk_mentee_reject')

    if request.method == 'POST':
        form = TalkMenteeForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.writer = request.user.profile
            article.nickname = request.user.profile.nickname
            article.save()
            return redirect(article)
    else:
        form = TalkMenteeForm()
    return render(request, 'lattors/talkmentee_form.html', {
        'form': form,
    })

def talk_mentee_detail(request, id):
    TalkMentee.objects.filter(id=id).update(hits=F('hits')+1)
    article = get_object_or_404(TalkMentee, id=id)
    next_article = TalkMentee.objects.filter(id__gt=article.id).order_by('id').first()
    previous_article = TalkMentee.objects.filter(id__lt=article.id).order_by('-id').first()
    
    return render(request, 'lattors/talkmentee_detail.html', {
        'article': article,
        'next_article': next_article,
        'previous_article': previous_article,
    })

@login_required
def talk_mentee_edit(request, id):
    article = get_object_or_404(TalkMentee, id=id)

    if request.user.profile.adminmentor == True:
        if request.user.is_superuser:
            if request.method == 'POST':
                form = TalkMenteeForm(request.POST, instance = article)
                if form.is_valid():
                    article = form.save(commit=False)
                    article.writer = request.user.profile
                    article.nickname = request.user.profile.nickname
                    article.save()
                    return redirect(article)
            else:
                form = TalkMenteeForm(instance = article)

            return render(request, 'lattors/talkmentee_edit.html', {
                'form': form,
            })
        else:
            return redirect('lattors:talk_mentee_reject')

    if request.method == 'POST':
        form = TalkMenteeForm(request.POST, instance = article)
        if form.is_valid():
            article = form.save(commit=False)
            article.writer = request.user.profile
            article.nickname = request.user.profile.nickname
            article.save()
            return redirect(article)
    else:
        form = TalkMenteeForm(instance = article)

    return render(request, 'lattors/talkmentee_edit.html', {
        'form': form,
    })

def talk_mentee_reject(request):
    return render(request, 'lattors/talkmentee_reject.html')

talk_mentee_delete = DeleteView.as_view(model = TalkMentee, success_url=reverse_lazy('lattors:talk_mentee'), pk_url_kwarg='id')