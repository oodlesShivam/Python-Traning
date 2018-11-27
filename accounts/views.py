from django.shortcuts import render, redirect
from datetime import datetime
# from accounts.forms import (RegistrationForm, EditProfileForm)
from accounts.forms import (RegistrationForm, EditProfileForm, ProfileForm)
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse


# Create your views here.
def home(request):
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
            return redirect('home:home')
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
        profile_form = ProfileForm(request.POST, instance=request.user.userprofile)

        if form.is_valid() and profile_form.is_valid():
            user_form = form.save()
            custom_form = profile_form.save(False)
            custom_form.user = user_form
            custom_form.save()

            return redirect('accounts:view_profile')
    else:
        form = EditProfileForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.userprofile)
        args = {}
        # args.update(csrf(request))
        args['form'] = form
        args['profile_form'] = profile_form
        return render(request, 'accounts/edit_profile.html', args)
# def edit_profile(request):
#     if request.method == 'POST':
#         form = EditProfileForm(request.POST, instance=request.user)
#         # profile_form = ProfileForm(request.POST, instance=request.user.userprofile)
#
#         if form.is_valid(): #and profile_form.is_valid():
#             form.save()
#             # profile_form.save()
#             return redirect('accounts:view_profile')
#     else:
#         form = EditProfileForm(instance=request.user)
#         # profile_form = ProfileForm(instance=request.user.userprofile)
#         args = {'form': form}
#         return render(request, 'accounts/edit_profile.html', args)

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