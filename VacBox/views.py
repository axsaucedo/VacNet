from django.shortcuts import render
from django import forms
from VacBox.models import VaccineCase
from VacBox.vactools import cryptolink
from django.forms.util import ErrorList
from django.core.urlresolvers import reverse


from django.http import HttpResponseRedirect
from django.db import models

def vacBox(request):
    return render(request, 'index.html')

def createCase(request):
    if request.method == 'POST': # If the form has been submitted...
        form = CaseForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            vaccines = form.cleaned_data['vaccines']
            country =  form.cleaned_data['country']
            password =  form.cleaned_data['password']

            CaseInstance = VaccineCase.objects.create(
                                                      vaccines=vaccines
                                                    , country=country
                                                    , password=password
                                                )
            CaseInstance.save()
            index = CaseInstance.caseid+10000
            casenumber = cryptolink.encrypt(index)

            return render(request, 'casecreated.html', {
                'vaccines': vaccines,
                'country': country,
                'casenumber': casenumber,

            }) # Redirect after POST
    else:
        form = CaseForm() # An unbound form

    return render(request, 'genericform.html', {
        'form': form,
        'name': "Create Case",
        })


def editCase(request, code):
    if(code == ""):
        return notFound(request)

    index = cryptolink.decrypt(code)-10000

    caseInstance = ""

    try:
        caseInstance = VaccineCase.objects.get(pk=index)
    except:
        return notFound(request)

    if request.method == 'POST': # If the form has been submitted...
        form = PasswordForm(request.POST) # A form bound to the POST data
        if form.is_valid() and (caseInstance.password == form.cleaned_data['password']): # All validation rules pass

            return HttpResponseRedirect('/e/'+code+'/')


    form = PasswordForm()

    if(form.is_valid() and caseInstance.password != form.cleaned_data['password']):
        errors = form._errors.setdefault("myfield", ErrorList())
        errors.append(u"Wrong Password")

    return render(request, 'genericform.html', {
        'form': form,
        'name': "Please enter case password",
    })

def addPeople(request, code):
    print "jello"
    if(code == ""):
        return notFound(request)

    index = cryptolink.decrypt(code)-10000

    caseInstance = ""

    try:
        caseInstance = VaccineCase.objects.get(pk=index)
    except:
        return notFound(request)

    if request.method == 'POST': # If the form has been submitted...
        form = PersonForm(request.POST) # A form bound to the POST data
        if form.is_valid():
            print "good"
            firstname = form.cleaned_data['firstname']
            lastname = form.cleaned_data['lastname']
            dob = form.cleaned_data['dob']
            gender = form.cleaned_data['gender']
            mobile = form.cleaned_data['mobile']
            guardian = form.cleaned_data['guardian']
            guardianmobile = form.cleaned_data['guardianmobile']
            vaccinetype = form.cleaned_data['vaccinetype']

            country = caseInstance.password
            vaccines = caseInstance.vaccines
            personForm = PersonForm()

            return render(request, 'genericform.html', {
                    'form': personForm,
                    'name': "Enter a person for case " + code,
                    'success': True,
                })
    else:
        form = PersonForm()

    return render(request, 'genericform.html', {
        'form': form,
        'name': "Enter a person for case " + code,
        'success': False,
        })


def notFound(request):
    return render(request, '404.html')


class CaseForm(forms.Form):
    vaccines = forms.IntegerField()
    country = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)

class PasswordForm(forms.Form):
    password = forms.CharField(max_length=100)

class PersonForm(forms.Form):
    firstname = forms.CharField(max_length=100)
    lastname = forms.CharField(max_length=100)
    dob = forms.DateField()
    gender = forms.CharField(max_length=1)
    mobile = forms.CharField(max_length=20)
    guardian = forms.CharField(max_length=100)
    guardianmobile = forms.CharField(max_length=100)
    vaccinetype = forms.CharField(max_length=100)




