from django.contrib.auth.models import User
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from home.forms import HomeForm
from home.models import Post


class HomeViews(TemplateView):
    template_name = 'home/home.html'

    def get(self, request):
        form = HomeForm()
        posts = Post.objects.all().order_by('-created')
        users = User.objects.all()
        args = {'form': form, 'posts': posts , 'users':users}
        response = render(request, self.template_name, args)
        response.delete_cookie('login_count')
        return response

    def post(self, request):
        form = HomeForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('home:home')
