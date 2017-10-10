from django.contrib import admin
from .models import Mentors, Mentee, Major

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