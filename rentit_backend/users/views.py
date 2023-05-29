from django.shortcuts import render, redirect
from django.views import View
from .forms import RegistrationForm


class RegistrationView(View):
    form_class = RegistrationForm
    template_name = 'registration.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data.get('password')
            user.set_password(password)
            user.save()
            return redirect('home')

        return render(request, self.template_name, {'form': form})