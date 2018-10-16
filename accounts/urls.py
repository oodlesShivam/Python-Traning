from django.conf.urls import patterns, url
from django.contrib.auth.views import login, logout , password_reset , password_reset_done, password_reset_confirm, password_reset_complete

urlpatterns = patterns('accounts.views',
                       url(r'^$', 'hello', name='hello'),
                       url(r'^login/$', login, {'template_name': 'accounts/login.html'} , name='login'),
                       url(r'^logout/$', logout, {'template_name': 'accounts/logout.html'} , name='logout'),
                       url(r'^register/$', 'register', name='register'),
                       url(r'^view_profile/$', 'view_profile', name ='view_profile'),
                       url(r'^view_profile/edit_profile/$', 'edit_profile', name ='edit_profile'),
                       url(r'^change-password/$', 'change_password', name ='chnage_password'),
                       url(r'^password-reset/$', password_reset, name ='password_reset'),
                       url(r'^password-reset/done/$', password_reset_done,{'template_name': 'accounts/reset_password.html', 'post_reset_redirect': 'accounts:password_reset_done', 'email_template_name': 'accounts/reset_password_email.html'}, name='password_reset_done'),
                       url(r'^password-reset/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',{'template_name': 'accounts/reset_password_done.html'}, password_reset_confirm, name='password_reset_confirm'),
                       url(r'^password-reset/complete/$', password_reset_complete, {'template_name': 'accounts/reset_password_complete.html'} ,name='password_reset_complete'),)