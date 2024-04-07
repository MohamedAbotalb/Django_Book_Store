from django.shortcuts import render, redirect, reverse

# Create your views here.


def profile_view(request):
    url = reverse('index_page')
    return redirect(url)
