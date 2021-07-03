from django.shortcuts import redirect, render
from django.views.generic import CreateView
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm


# class UserCreateView(CreateView):
#     model = User
#     form_class = UserCreationForm
#     template_name = "form.html"
#     success_url = "/"


def user_register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name='Staff')
            user.groups.add(group)
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, template_name='form.html', context={'form': form})