from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def teamDetails(request):
    return HttpResponse("E sala cup namde")

def display(request):
    template=loader.get_template('hello.html')
    return HttpResponse(template.render())


def myplayer_list(request):
    myplayer = TeamDetails.objects.all()
    return render(request, 'rcb/myplayer-list.html',{'myplayer': myplayer})
