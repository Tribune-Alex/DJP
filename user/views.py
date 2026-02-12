from django.shortcuts import render
from django.views.generic import CreateView,UpdateView
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from user.forms import CustomUserForm,ProfileUpdateForm,UserUpdateForm
from django.contrib.auth.mixins import LoginRequiredMixin
from user.models import Profile
from django.urls import reverse_lazy

class UserRegisterView(CreateView):
    model = User
    template_name = 'register.html'
    form_class = CustomUserForm
    success_url = '/'
    
    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_staff = True
        user.save()
        return super().form_valid(form)
    
class UserLoginView(LoginView):
    template_name = 'login.html'
    next_page = '/'


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = 'profile.html'
    success_url = reverse_lazy('user:profile')

    def get_object(self):
        return self.request.user

    def get_profile_instance(self):
        profile, created = Profile.objects.get_or_create(user=self.request.user)
        return profile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = self.get_profile_instance()

        
        if 'profile_form' not in context:
            context['profile_form'] = ProfileUpdateForm(instance=profile)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        
        user_form = self.get_form(self.get_form_class())
        
        profile_form = ProfileUpdateForm(request.POST, instance=self.get_profile_instance())

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return super().form_valid(user_form)
        else:
            return self.render_to_response(
                self.get_context_data(form=user_form, profile_form=profile_form)
            )