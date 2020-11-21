from django.shortcuts import redirect, render
from django.views.generic import TemplateView, UpdateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
# from .models import Profile
# from .forms import ProfileForm
from django.contrib.auth import get_user_model, login as auth_login
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import auth, messages
from .models import User
from .forms import SignupForm


# class ProfileView(LoginRequiredMixin, TemplateView): # login_required
#     template_name = 'accounts/profile.html'

# profile = ProfileView.as_view()


# @login_required
# def profile_edit(request):
#     try:
#         profile = request.user.profile
#     except Profile.DoesNotExist:
#         profile = None

#     if request.method == "POST":
#         form = ProfileForm(request.POST, request.FILES, instance=profile)
#         if form.is_valid():
#             form.save(commit=False)
#             profile.user = request.user
#             profile.save()
#             return redirect('profile')
#     else:
#         form = ProfileForm()
#     return render(request, 'accounts/profile_form.html',{'form': form,})

# User = get_user_model() # get user model





# # 회원 가입
def signup(request):
#     # signup 으로 POST 요청이 왔을 때, 새로운 유저를 만드는 절차를 밟는다.
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "회원가입을 환영합니다.")
            return redirect('accounts/login')
    else:
        form = SignupForm()
    return render(request, "accounts/signup_form.html",{'form':form,})

# 로그인
def login(request):
    # login으로 POST 요청이 들어왔을 때, 로그인 절차를 밟는다.
    if request.method == 'POST':
        # login.html에서 넘어온 username과 password를 각 변수에 저장한다.
        username = request.POST['username']
        password = request.POST['password']
    
        # 해당 username과 password와 일치하는 user 객체를 가져온다.
        user = auth.authenticate(request, username=username, password=password)
        
        # 해당 user 객체가 존재한다면
        if user is not None:
            # 로그인 한다
            auth.login(request, user)
            return redirect('/')
        # 존재하지 않는다면
        else:
            # 딕셔너리에 에러메세지를 전달하고 다시 login.html 화면으로 돌아간다.
            return render(request, 'accounts/login_form.html', {'error' : 'username or password is incorrect.'})
    # login으로 GET 요청이 들어왔을때, 로그인 화면을 띄워준다.
    else:
        return render(request, 'accounts/login_form.html')

# 로그 아웃
def logout(request):
    # logout으로 POST 요청이 들어왔을 때, 로그아웃 절차를 밟는다.
    if request.method == 'POST':
        auth.logout(request)
        return redirect('/')

    # logout으로 GET 요청이 들어왔을 때, 로그인 화면을 띄워준다.
    return render(request, 'accounts/login.html')