from django.http import HttpResponse


def home_page(request):
    return HttpResponse("This is the home page.")


def about(request):
    return HttpResponse("This is the about page.")
