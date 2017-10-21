from django.contrib import admin
from .models import Mentors, Mentee, Major, ActPhoto, TalkMentor, TalkMentee

@admin.register(Mentors)
class MentorsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'school', 'major', 'sub_major', 'grade']
    list_display_links = ['name']
    search_fields = ['school','major']
    list_filter = ['school','major','grade']


@admin.register(Mentee)
class MenteeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'grade', 'school_expect']
    list_display_links = ['name']
    search_fields = ['school_expect', 'major_expect']
    list_filter = ['grade', 'school_expect', 'major_expect']


@admin.register(Major)
class MajorAdmin(admin.ModelAdmin):
    list_display = ['major']


@admin.register(ActPhoto)
class ActPhotoAdmin(admin.ModelAdmin):
    list_display = ['id', 'site', 'year', 'date']
    list_display_links = ['site']


@admin.register(TalkMentor)
class TalkMentorAdmin(admin.ModelAdmin):
    list_display = ['nickname', 'title', 'created_at', 'updated_at']
    list_display_links = ['title']
    search_fields = ['nickname', 'title']
    list_filter = ['nickname']


@admin.register(TalkMentee)
class TalkMenteeAdmin(admin.ModelAdmin):
    list_display = ['nickname', 'title', 'created_at', 'updated_at']
    list_display_links = ['title']
    search_fields = ['nickname', 'title']
    list_filter = ['nickname']