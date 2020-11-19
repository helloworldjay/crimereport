from django.shortcuts import redirect, render
from django.views.generic import TemplateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Profile
from .forms import ProfileForm


class ProfileView(LoginRequiredMixin, TemplateView): # login_required
    template_name = 'accounts/profile.html'

profile = ProfileView.as_view()


# get Error in case of no data
# class ProfileUpdateView(LoginRequiredMixin, UpdateView):
#     model = Profile
#     form_class = ProfileForm

# profile_edit = ProfileUpdateView.as_view()

@login_required
def profile_edit(request):
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        profile = None

    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('profile')
    else:
        form = ProfileForm()
    return render(request, 'accounts/profile_form.html',{'form': form,})