from django.shortcuts import render, redirect
from datetime import date
from datetime import time
from datetime import datetime
from myapp.models import Dreamreal
from django.http import HttpResponse
from django.core.mail import send_mail
from django.core.mail import send_mass_mail
from django.template.loader import get_template
from django.template import Context
from django.template.loader import render_to_string


# Create your views here.

def hello(request):
    today = datetime.now().date()
    daysOfWeek = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    return render(request, "hello.html", {"today": today, "days_of_week": daysOfWeek})


def login(request):
    return render(request, "login.html", {})


def viewArticle(request, articleId):
    text = "Displaying article Number : %s" % articleId
    return redirect('articles', year="2045", month="02")


def viewArticles(request, month, year):
    text = "Displaying articles of : %s/%s" % (year, month)
    return HttpResponse(text)


def crudops(request):
    # Creating an entry

    dreamreal = Dreamreal(
        website="www.polo.com", mail="sorex@polo.com",
        name="sorex", phonenumber="002376970"
    )

    dreamreal.save()

    # Read ALL entries
    objects = Dreamreal.objects.all()
    res = 'Printing all Dreamreal entries in the DB : <br>'

    for elt in objects:
        res += elt.name + "<br>"

    # Read a specific entry:
    sorex = Dreamreal.objects.get(name="sorex")
    res += 'Printing One entry <br>'
    res += sorex.name

    # Delete an entry
    res += '<br> Deleting an entry <br>'
    sorex.delete()

    # Update
    dreamreal = Dreamreal(
        website="www.polo.com", mail="sorex@polo.com",
        name="sorex", phonenumber="002376970"
    )

    dreamreal.save()
    res += 'Updating entry<br>'

    dreamreal = Dreamreal.objects.get(name='sorex')
    dreamreal.name = 'thierry'
    dreamreal.save()

    return HttpResponse(res)


def datamanipulation(request):
    res = ''

    # Filtering data:
    qs = Dreamreal.objects.filter(name="paul")
    res += "Found : %s results<br>" % len(qs)

    # Ordering results
    qs = Dreamreal.objects.order_by("name")

    for elt in qs:
        res += elt.name + '<br>'

    return HttpResponse(res)


def sendSimpleEmail(request, emailto):
    res = send_mail("subject", "content", "shivam4848@gmail.com", [emailto],
                    html_message="<strong>Comment tu vas?</strong>")
    print(emailto)
    if res == 1:
        return HttpResponse("Your mail is sent")
    else:
        return HttpResponse("your mail is not sent")


def sendMassEmail(request, emailto1, emailto2):
    msg1 = ('subject 1', 'message 1', 'polo@polo.com', [emailto1])
    msg2 = ('subject 2', 'message 2', 'polo@polo.com', [emailto2])
    res = send_mass_mail((msg1, msg2), fail_silently=False)
    return HttpResponse('%s' % res)


def sendHtmlEmail(request):
    today = datetime.now().date()
    daysOfWeek = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    res = send_mail('Thanks for signing up!',
                    render_to_string("check.html", {"today": today, "days_of_week": daysOfWeek}),
                    "shivam4848@gmail.com", ["shivam4848@gmail.com"], fail_silently=True)
    return HttpResponse(res)
