from django.shortcuts import render, redirect
from datetime import datetime
from accounts.forms import RegistrationForm


# Create your views here.
def hello(request):
    today = datetime.now().date()
    daysOfWeek = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    return render(request, "accounts/hello.html", {"today": today, "days_of_week": daysOfWeek})


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
