from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.shortcuts import redirect, render
from member.forms import MemberLoginForm, MemberSignupForm
from .models import Member


def login(request):
    if request.method == 'POST':
        form = MemberLoginForm(request.POST, label_suffix='')
        if form.is_valid():
            member_id = form.cleaned_data.get('member_id')
            password = form.cleaned_data.get('password')
            user = authenticate(member_id=member_id, password=password)

            if user is not None and user.is_active:
                auth_login(request, user)
                return redirect('image:index')
    else:
        form = MemberLoginForm(label_suffix='')

    return render(request, 'member/login.html', {'form': form})


def logout(request):
    auth_logout(request)
    return render(request, 'image/index.html')


def signup(request):
    if request.method == 'POST':
        form = MemberSignupForm(request.POST, label_suffix='')
        if form.is_valid():
            data = form.cleaned_data
            member_id = data.get('member_id')
            password1 = data.get('password1')
            password2 = data.get('password2')
            name = data.get('name')

            user = Member.objects.create_user(member_id=member_id,
                                              password=password1,
                                              name=name,)
            auth_login(request, user)
            return render(request, 'image/index.html')
    else:
        form = MemberSignupForm(label_suffix='')
    return render(request, 'member/signup.html', {'form': form})
