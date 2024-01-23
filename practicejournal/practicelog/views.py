from django.shortcuts import render


def homeScreen(request):
    return render(request, "base.html")
