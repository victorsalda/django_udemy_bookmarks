from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.contrib.auth.decorators import login_required

def user_login (request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username =cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return HttpResponse ('Authenticated successfully')
                else:
                    return HttpResponse ('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()

            # render: combines a given template with a given context dictionary
            # and returns an HttpResponse object with that rendered text.
    return render (request, 'account/login.html', {'form': form}) # request: the request object used to generate th9s response.
                                                                  # template_name: the full name of a template to use or sequence of template names.
                                                                  # dictionary.
@login_required() #this check is the currect user is authenticated.
def dashboard (request):
    return render(request,'account/dashboard.html',{'section': 'dashboard'})

