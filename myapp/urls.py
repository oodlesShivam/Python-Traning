from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

urlpatterns = patterns('myapp.views',
                       url(r'^hello/', 'hello', name='hello'),
                       url(r'^login/', 'login', name='login'),
                       url(r'^article/(\d+)/', 'viewArticle', name='article'),
                       url(r'^articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})', 'viewArticles', name='articles'),
                       url(r'^crudops/', 'crudops', name='crudops'),
                       url(r'^simpleemail/(?P<emailto>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/', 'sendSimpleEmail',
                           name='sendSimpleEmail'),
                       url(
                           r'^massEmail/(?P<emailto1>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/(?P<emailto2>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})',
                           'sendMassEmail', name='sendMassEmail'),
                       url(r'^htmlmail/', 'sendHtmlEmail', name='sendHtmlEmail'), )
