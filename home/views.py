from django.views.generic import TemplateView
from django.shortcuts import render
from home.forms import HomeForm


class HomeViews(TemplateView):
    template_name = 'home/home.html'

    def get(self, request):
        form = HomeForm()
        response =  render(request, self.template_name, {'form':form})
        response.delete_cookie('login_count')
        return response