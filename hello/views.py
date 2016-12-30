from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

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

@csrf_exempt
def github(request):
    if request.method == 'GET':
        return _show_requests(request)
    else:
        return _new_request(request)


def _new_request(request):
    push_event = PushEvent()
    push_event.payload = request.body
    push_event.new = True
    push_event.save()
    return HttpResponse("This is the github route")


def _show_requests(request):
    push_events = PushEvent.objects.all()
    json_events = [json.loads(pe.payload) for pe in push_events]
    return JsonResponse({'data': json_events})
