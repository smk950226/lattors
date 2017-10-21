from django.contrib import admin
from .models import Mentor,Profile

@admin.register(Mentor)
class MentorAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'name', 'school', 'major', 'sub_major', 'grade']
    list_display_links = ['name']
    search_fields = ['school','major']
    list_filter = ['school','major','grade']


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['name', 'nickname', 'emailaddress', 'adminmentor']
    list_display_links = ['nickname']
    search_fields = ['nickname']