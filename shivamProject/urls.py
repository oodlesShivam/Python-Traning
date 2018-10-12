from django.conf.urls import include, url
from django.contrib import admin
from shivamProject import views

urlpatterns = [
    url(r'^$', views.login_redirect, name='login_redirect'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^myapp/', include('myapp.urls')),
    url(r'^accounts/', include('accounts.urls'))
]
