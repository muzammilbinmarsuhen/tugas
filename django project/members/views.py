#views members
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
    template  = loader.get_template('index.html')
    return HttpResponse(template.render())

def blog(request):
    template  = loader.get_template('blog.html')
    return HttpResponse(template.render())

def jadwal_m(request):
    template = loader.get_template('jadwal_m.html')
    return HttpResponse(template.render())

def jadwal_t(request):
    template = loader.get_template('jadwal_t.html')
    return HttpResponse(template.render())

def jadwal_t(request):
    template = loader.get_template('jadwal_t.html')
    return HttpResponse(template.render())

def jadwal_m(request):
    template = loader.get_template('jadwal_m.html')
    return HttpResponse(template.render())

def hiburan(request):
    template = loader.get_template('hiburan.html')
    return HttpResponse(template.render())