from django import forms
from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from chat.forms import UserForm, UserUpdateForm
from django.contrib import messages

# Create your views here.


def main_view(request):
    context = {}
    if request.session.has_key('username'):
        username = request.session['username']
        return render(request, 'chat/main.html', {'username': username})
    else:
        return redirect('/login')


def register_view(request):
    context = {}
    if request.method == 'POST':
        form = UserForm(request.POST)
        print(form.errors)
        if form.is_valid():
            print("inside valid form")
            form.save()
            return redirect('/login')
        else:
            print('Outside is_valid')
    else:
        form = UserForm()
    return render(request, 'chat/register.html', {'form': form})


def login_view(request):
    context = {}
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            print(f"{username}")
            request.session['username'] = username
            return redirect('/letschat')
    else:
        form = AuthenticationForm()
    return render(request, 'chat/login.html', {'form': form})


def logout_view(request):
    try:
        del request.session['username']
    except:
        pass
    #HttpResponse("<strong>You are logged out.</strong>")
    return redirect('/home')


def home_view(request):
    context = {}
    return render(request, 'chat/index.html', context=context)


def update_view(request):
    update_form = None
    if request.method == 'POST':
        update_form = UserUpdateForm(request.POST, instance=request.user)
        if update_form.is_valid():
            update_form.save()
            messages.success(
                request, f'Your Account has been successfully updated!')
            return redirect('/letschat')
    else:
        print("The update request failed.")
    context = {'u_form': update_form}
    return render(request, 'chat/update-profile.html', context)
