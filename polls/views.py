from django.http import HttpResponse


def index(request):
    return HttpResponse("Volim sarmu vise nego slaninu.")
