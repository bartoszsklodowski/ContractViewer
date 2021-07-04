from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import CreateView
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm


class UserRegisterView(View):
    def get(self, request):
        form = UserCreationForm()
        return render(
            request,
            template_name="form.html",
            context={"form": form}
        )

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name='Staff')
            user.groups.add(group)
            return redirect('login')
        return render(
            request,
            template_name="form.html",
            context={"form": form}
        )
