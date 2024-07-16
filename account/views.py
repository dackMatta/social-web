from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .form import LoginForm, UserRegistrationForm,UserEditForm, ProfileEditForm
from .models import Profile
from django.contrib import messages


@login_required
def user_list(request):
    users=User.objects.filter(is_active=True)
    return render(request,
                  'account/user/list.html',
                  {'section':'people',
                   'users':users})


@login_required
def user_detail(request, username):
    user=get_object_or_404(User,
                           username=username,
                           is_active=True)
    return render(request,
                  'account/user/detail.html',
                  {'section':'people',
                   'user':user})

@login_required
def dashboard(request):
    state={'section':dashboard}
    return render(request,
                  'account/dashboard.html',
                  state)

def user_login(request):
    if request.method == 'POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            user=authenticate(request,
                              username=cd['username'],
                              password=cd['password'])
            
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return HttpResponse('Authenticated successfully')
                
                else:
                    return HttpResponse('Disabled account')

            else:
                return HttpResponse('Invalid login')   
        
    else:
        form=LoginForm()
        
    stem={'form': form}
    return render(request,'account/login.html',stem)

def register(request):
    if request.method == 'POST':
        user_form=UserRegistrationForm(request.POST)
        if user_form.is_valid():
            #create a new user and commit save to false 
            new_user=user_form.save(commit=False)
            #save the new user choosen password
            new_user.set_password(user_form.cleaned_data['password'])
            #save the new user object
            new_user.save()
            #create the user profile
            Profile.objects.create(user=new_user)
            steem={'new_user': new_user}
            return render(request,
                          'account/register_done.html',steem)

    else:
         user_form=UserRegistrationForm()
           

    feel={'user_form':user_form}    
    return render(request,
                  'account/register.html',feel)   

@login_required
def edit(request):
    if request.method == 'POST':
        user_form=UserEditForm(instance=request.user,
                               data=request.POST)
        profile_form=ProfileEditForm(instance=request.user.profile,
                                     data=request.POST,
                                     files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request,'Profile updated successfully')
        else:
            messages.error(request,'Error updating your profile')

    else:
        user_form=UserEditForm(instance=request.user)
        profile_form=ProfileEditForm(instance=request.user.profile)

    peel={'user_form':user_form,
          'profile_form':profile_form}
    return render(request,
                  'account/edit.html',peel)
                          

                    
            

            

     


