from django.shortcuts import render
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout# defining login function and logout function
# from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm, CustomErrorList
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def logout(request):
    auth_logout(request)
    return redirect('home.index')

def login(req):
    template_data = {}
    template_data['title'] = 'Login'
    if req.method == 'GET':
        return render(req, 'accounts/login.html', {'template_data': template_data})
    elif req.method =='POST':
        user = authenticate(req, username = req.POST['username'], password = req.POST['password'])
        if user is None:
            template_data['error'] = 'The username or password is incorrect.'
            return render(req, 'accounts/login.html', {'template_data': template_data})
        else:
            auth_login(req, user)
            return redirect('home.index')

def signup(req):
    template_data = {}
    template_data['title'] = 'Sign up'

    if req.method == 'GET':
        template_data['form'] = CustomUserCreationForm()
        return render(req, 'accounts/signup.html', {'template_data': template_data})
    elif req.method == 'POST':
        form = CustomUserCreationForm(req.POST, error_class=CustomErrorList)
        if form.is_valid():
            form.save()
            return redirect('accounts.login')
        else:
            template_data['form'] = form
            return render(req, 'accounts/signup.html', {'template_data': template_data})