from django.shortcuts import render, redirect, reverse
from accounts.forms import RegistrationForm


# Create your views here.


def profile_view(request):
    url = reverse('index_page')
    return redirect(url)


def register_user(request):
    form = RegistrationForm()
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login_url = reverse('login')
            return redirect(login_url)

    return render(request, 'accounts/register.html', {'form': form})
