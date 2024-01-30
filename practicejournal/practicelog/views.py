from django.shortcuts import render


def homeScreen(request):
    return render(request, "home.html")
