from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting, PushEvent

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, 'index.html')


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})


def github(request):
    if request.method == 'GET':
        return _show_requests(request)
    else:
        return _new_request(request)


def _new_request(request):
    push_event = PushEvent()
    push_event.payload = request.body
    push_event.save()
    return HttpResponse("This is the github route")


def _show_requests(request):
    push_events = PushEvent.objects.all()
    return render(request, 'push_events.html', {'push_events': push_events})
