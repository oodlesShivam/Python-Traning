from django.conf.urls import patterns, url
from django.contrib.auth.views import login, logout

urlpatterns = patterns('accounts.views',
                       url(r'^$', 'hello', name='hello'),
                       url(r'^login/$', login, {'template_name': 'accounts/login.html'}),
                       url(r'^logout/$', logout, {'template_name': 'accounts/logout.html'}),
                       url(r'^register/$', 'register', name='register'), )
