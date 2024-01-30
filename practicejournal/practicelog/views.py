from django.shortcuts import render


def homeScreen(request):
    return render(request, "home.html")


def practiceScreen(request):
    return render(request, "practice.html")
