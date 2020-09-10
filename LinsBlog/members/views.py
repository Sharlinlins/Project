from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic import DetailView, CreateView
from django.urls import reverse_lazy
from .forms import SignUpForm, EditProfileForm, PasswordChangingForm, ProfilePageForm,EditProfilePageForm, EditProfileStaffForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from myblog.models import Profile
from django.contrib import messages
 

class ShowProfilePageView(DetailView):
    model = Profile
    template_name = 'registration/userprofile.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        context["page_user"] = page_user
        return context

class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangingForm
    # form_class = PasswordChangeForm
    # template_name='registration/changepassword.html'
    success_url = reverse_lazy('password_success')

def password_success(request):
    return render(request, 'registration/password_success.html', {})

class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/editprofile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user

class UserEditStaffView(generic.UpdateView):
    form_class = EditProfileStaffForm
    template_name = 'registration/editprofilestaff.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user
    
class EditProfilePageView(generic.UpdateView):
    model = Profile
    form_class = EditProfilePageForm
    template_name = 'registration/editprofilepage.html'

class CreateProfilePageView(CreateView):
    model = Profile
    form_class = ProfilePageForm
    template_name = 'registration/createprofilepage.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)