from django.conf.urls import url
from home.views import HomeViews

urlpatterns=[
    url(r'^$', HomeViews.as_view(), name='home')
]