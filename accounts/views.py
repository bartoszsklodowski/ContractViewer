from django.contrib.auth import login
from django.contrib.auth.views import PasswordResetView
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View
from django.views.generic import CreateView
from django.contrib.auth.models import User, Group
from accounts.forms import CustomEmailValidationOnForgotPassword, CustomUserCreationForm


def dashboard(request):
    return render(request, "dashboard.html")


class UserResetPasswordView(PasswordResetView):
    form_class = CustomEmailValidationOnForgotPassword
    template_name = "registration/password_reset_form.html"


class UserRegisterView(View):

    def get(self, request):
        form = CustomUserCreationForm()
        return render(
            request,
            template_name="register.html",
            context={"form": form}
        )

    def post(self, request):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.backend = "django.contrib.auth.backends.ModelBackend"
            user.save()
            if Group.objects.filter(name='Staff').exists():
                group = Group.objects.get(name='Staff')
                user.groups.add(group)
            login(request, user)
            return redirect(reverse('login'))
        return render(
            request,
            template_name="register.html",
            context={"form": form}
        )
