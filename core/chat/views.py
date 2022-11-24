from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.views.generic import CreateView

from .forms import UserCreationForm
from .models import User


class Register(CreateView):
    template_name = 'registration/register.html'

    # get registration form.
    def get(self, request):
        context = {
             'form': UserCreationForm()
            }
        return render(request, self.template_name, context)

    # Save user to database.
    def post(self, request):

        form = UserCreationForm(request.POST)

        # check validity of form data.
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')

            # autologin on service
            user = authenticate(username=username, password=password)
            login(request, user)

            return redirect('main')

        # if form not valid.
        context = {
            'form': form
        }
        return render(request, self.template_name, context)


def index(request):
    users = User.objects.all()
    return render(request, 'main.html', {'users': users})


def chat_room(request, chat_name):
    return render(request, 'room.html', {'chat_name': chat_name})
