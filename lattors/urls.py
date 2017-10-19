from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.main, name='main'),
    url(r'^admin/mentor', views.admin_mentor, name='admin_mentor'),
    url(r'^admin/mentee', views.admin_mentee, name='admin_mentee'),
    url(r'^intro/$',views.intro, name='comp_intro'),
    url(r'^mentorlist/$',views.mentors_list, name='mentor_list'),
    url(r'^mentorlist/(?P<id>\d+)/$',views.mentor_detail, name='mentor_detail'),
    url(r'^vision/$',views.vision, name="comp_vision"),
    url(r'^member/$',views.member, name="comp_member"),
    url(r'^contact/$',views.contact, name="comp_contact"),
    url(r'^act/$',views.act_list, name='act_list'),
    url(r'^act/lattors/$',views.act_lattors, name='act_lattors'),
    url(r'^act/comma/$',views.act_comma, name='act_comma'),
    url(r'^act/photo/$',views.act_photo, name='act_photo'),
    url(r'^act/photo/add$',views.act_photo_add, name='act_photo_add'),
    url(r'^talk/mentor/$',views.talk_mentor, name='talk_mentor'),
    url(r'^talk/mentor/new/$',views.talk_mentor_new, name='talk_mentor_new'),
    url(r'^talk/mentor/(?P<id>\d+)/$',views.talk_mentor_detail, name='talk_mentor_detail'),
    url(r'^talk/mentor/(?P<id>\d+)/edit/$',views.talk_mentor_edit, name='talk_mentor_edit'),
    url(r'^talk/mentor/(?P<id>\d+)/delete/$',views.talk_mentor_delete, name='talk_mentor_delete'),
    #url(r'^talk/mentee/$',views.talk_mentee, name='talk_mentee'),
]