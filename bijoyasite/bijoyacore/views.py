from django.http import HttpResponse


def index(request):
    return HttpResponse("Yeah everything's working alright")
