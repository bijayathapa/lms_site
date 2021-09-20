
from django.shortcuts import render
from .models import *
# Create your views here.


def index(request):
    courses = Course.objects.all()
    context = {
        'courses': courses,
    }
    return render(request, 'index.html', context)

def contact(request):
    context = {}
    return render(request, 'contact.html', context)

def course(request):
    courses = Course.objects.all()
    context = {
        'courses': courses,
    }
    return render(request, 'course.html', context)

def courseDetail(request):
    context = {}
    return render(request, 'course-detail.html', context)

def gallery(request):
    context = {}
    return render(request, 'gallery.html', context)
