from django.shortcuts import render, redirect
from . import forms
#
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
# Create your views here.
def index(request):
    return render(request, 'kreiva/index.html')

def register(request):
    registered = False

    if request.method == 'POST':
        user_form = forms.UserForm(data=request.POST)

        if user_form.is_valid()  and user_form.cleaned_data['password'] == user_form.cleaned_data['confirm_password']:
            user = user_form.save()
            user.set_password(user.password)
            user.save()




            return redirect('/kreiva/login/')
        elif user_form.data['password'] != user_form.data['confirm_password']:
            user_form.add_error('confirm_password', 'The passwords do not match')
        else:
                print(user_form.errors)


    else:
            user_form = forms.UserForm()

    return render(request, "kreiva/registration.html", {'registered': registered, 'user_form': user_form
                                                            })

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")
        else:
            print("Someone tried to login and failed")
            print("Username: {} and Password: {}".format(username, password))
            return HttpResponse("Invalid login details supplied")
    return render(request, 'kreiva/login.html', {})
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def special(request):
    return HttpResponse("You are logged In, Nice!")

