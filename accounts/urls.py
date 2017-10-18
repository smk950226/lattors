from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^login/$',views.login, name='login'),
    url(r'^logout/$',auth_views.logout, name='logout', kwargs = {
        'next_page': '/',
    }),
    url(r'^signup/$',views.signup, name='signup'),
    url(r'^profile/$',views.profile, name='profile'),
    url(r'^admin/mentor/$',views.admin_mentor, name='admin_mentor'),
    #url(r'^social/signup/$',views.mysignup, name='mysignup')
]