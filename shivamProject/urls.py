from django.conf.urls import include, url
from django.contrib import admin
from shivamProject import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  url(r'^$', views.login_redirect, name='login_redirect'),
                  url(r'^admin/', include(admin.site.urls)),
                  url(r'^accounts/', include('accounts.urls', namespace='accounts')),
                  url(r'^home/', include('home.urls', namespace='home'))

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
