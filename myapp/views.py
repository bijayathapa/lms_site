
from myapp.decorators import unauthenticated_user
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.contrib import messages

from .forms import CreateUserForm
from .decorators import unauthenticated_user, allowed_users

from .models import *
# Create your views here.


def index(request):
    courses = Course.objects.all()
    teachers = Teacher.objects.all()
    context = {
        'courses': courses,
        'teachers': teachers,
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

@login_required(login_url='login')
@allowed_users(allowed_roles=['teacher', 'admin'])
def uploadCourse(request):
    context = {}
    return render(request, 'uploadcourse.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'teacher'])
def writeBlog(request):
    context = {}
    return render(request, 'writeblog.html', context)


@unauthenticated_user
def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)

        if form.is_valid():
            user = form.save()

            username = form.cleaned_data.get('username')

            group = Group.objects.get(name = 'teacher')
            user.groups.add(group)
            messages.success(request, 'Account has been created for ' + username)
            return redirect('login')

    context = {
        'form':form,
        }
    return render(request, 'register.html', context)

@unauthenticated_user
def login(request):

	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(request, username = username, password = password)
		
		if user is not None:
			auth_login(request, user)
			return redirect('index')
		else:
			messages.info(request, 'Username OR Password is incorrect')
	context = {

	}

	return render(request, 'login.html', context)

def logoutUser(reqest):
    logout(reqest)
    return redirect('index')