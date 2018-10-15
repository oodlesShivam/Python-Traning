from django.conf.urls import patterns, url
from django.contrib.auth.views import login, logout

urlpatterns = patterns('accounts.views',
                       url(r'^$', 'hello', name='hello'),
                       url(r'^login/$', login, {'template_name': 'accounts/login.html'}),
                       url(r'^logout/$', logout, {'template_name': 'accounts/logout.html'}),
                       url(r'^register/$', 'register', name='register'),
                       url(r'^view_profile/$', 'view_profile', name ='view_profile'),
                       url(r'^view_profile/edit_profile/$', 'edit_profile', name ='edit_profile'),
                       url(r'^change-password$', 'change_password', name ='chnage_password'),)

