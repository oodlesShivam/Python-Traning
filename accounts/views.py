from django.shortcuts import render, redirect
from datetime import datetime
from accounts.forms import (RegistrationForm, EditProfileForm )
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required


# Create your views here.
def hello(request):
    today = datetime.now().date()
    daysOfWeek = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    response =  render(request, "accounts/hello.html", {"today": today, "days_of_week": daysOfWeek})
    response.delete_cookie('login_count')
    return response

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if (form.is_valid()):
            form.save()
            return redirect('/accounts')
    else:
        form = RegistrationForm()
        args = {'form': form}
        return render(request, 'accounts/reg_form.html', args)

@login_required
def view_profile(request):
    args = {'user': request.user}
    return render(request, 'accounts/view_profile.html', args)

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return render(reverse('accounts:view_profile'))
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'accounts/edit_profile.html', args)

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request , form.user)
            return render(request, 'accounts/view_profile.html')
    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form': form}
        return render(request, 'accounts/edit_profile.html', args)