from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

from webapp.forms import PersonalInfoItem
from webapp.models import PersonalInfo


def add_info(request):
    form = PersonalInfoItem()
    if request.method == 'POST':
        form = PersonalInfoItem(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        personalinfo = PersonalInfo()
        personalinfo.Name = cd['name']
        personalinfo.PhoneNum = cd['phoneNum']
        personalinfo.Email = cd['email']
        personalinfo.Job = cd['job']
        personalinfo.company = cd['company']
        personalinfo.Location = cd['location']
        personalinfo.save()
        return HttpResponseRedirect('/add_info_success/')
    else:
        return render_to_response('add_info.html', context_instance=RequestContext(request))


def add_info_success(request):
    return render_to_response('add_info_success.html')