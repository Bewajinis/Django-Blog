import re
from django.shortcuts import redirect, render
from django.views import View
from .form import UserRegisterForm

class RegisterView(View):
    def get(self, request):
        form = UserRegisterForm()
        return render(request, 'register.html', {'form': form})

    def post(self, request):
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('index')
        return render(request, 'register.html', {'form': form})