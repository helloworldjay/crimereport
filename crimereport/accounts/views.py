from django.shortcuts import redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model, login as auth_login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import auth, messages
from .models import User
from .forms import SignupForm
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView
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


# # 회원 가입
def signup(request):
#     # signup 으로 POST 요청이 왔을 때, 새로운 유저를 만드는 절차를 밟는다.
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            signed_user = form.save()
            auth_login(request, signed_user, backend='django.contrib.auth.backends.ModelBackend')
            messages.success(request, "회원가입을 환영합니다.")
            next_url = request.GET.get('next', 'postlist')
            return redirect(next_url)
    else:
        form = SignupForm()
    return render(request, "accounts/signup_form.html",{'form':form,})

# 로그인
login = LoginView.as_view(template_name="accounts/login_form.html")

# 로그 아웃
def logout(request):
    # logout으로 POST 요청이 들어왔을 때, 로그아웃 절차를 밟는다.
    if request.method == 'POST':
        messages.success(request, '로그아웃되었습니다.')
        auth.logout(request)
        return redirect('/')

    # logout으로 GET 요청이 들어왔을 때, 로그인 화면을 띄워준다.
    return render(request, 'accounts/login.html')