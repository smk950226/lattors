from django.contrib import admin
from .models import Mentor,MyUser

@admin.register(Mentor)
class MentorAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'name', 'school', 'major', 'sub_major', 'grade']
    list_display_links = ['name']
    search_fields = ['school','major']
    list_filter = ['school','major','grade']


@admin.register(MyUser)
class MyUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'nickname', 'email']
    list_display_links = ['nickname']
    search_fields = ['nickname']