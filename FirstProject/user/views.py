from django.shortcuts import render, redirect
from .models import User
from .forms import RegisterForm

def register(request):
    register_form = RegisterForm()
    context = {'forms' : register_form}

    if request.method == 'GET':
        return render(request, 'user/register.html', context)
    elif request.method == 'POST':
        user_id = request.POST.get('id','')
        user_pw = request.POST.get('pw', '')
        user_pw_confirm = request.POST.get('pw-confirm', '')
        print('user_pw_confirm',user_pw_confirm)
        user_name = request.POST.get('name', '')
        user_email = request.POST.get('email', '')

        if (user_id or user_pw or user_pw_confirm or user_name) == '':
            print('user_id,pw,name')
            return redirect('/user/register')
        elif user_pw != user_pw_confirm:
            print(user_pw)
            print(user_pw_confirm)
            print('pw fail')
            return redirect('/user/register')
        else:
            user = User(
                user_id = user_id,
                user_pw = user_pw,
                user_name = user_name,
                user_email = user_email
            )
            user.save()
        return redirect('/')
