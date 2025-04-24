# from django.shortcuts import render, redirect, get_object_or_404
# from django.contrib.auth.decorators import login_required, user_passes_test
# from .models import Event, Registration

# @login_required
# def event_list(request):
#     events = Event.objects.all()
#     return render(request, 'event/event_list.html', {'events': events})


# @user_passes_test(lambda u: u.is_superuser)
# def create_event(request):
#     if request.method == 'POST':
#         Event.objects.create(
#             name=request.POST['name'],
#             description=request.POST['description'],
#             event_date=request.POST['event_date'],
#             created_by=request.user
#         )
#         return redirect('event_list')
#     return render(request, 'event/create_event.html')


# @login_required
# def register_event(request, event_id):
#     event = get_object_or_404(Event, id=event_id)
#     Registration.objects.get_or_create(user=request.user, event=event)
#     return redirect('event_list')


# @login_required
# def cancel_registration(request, event_id):
#     Registration.objects.filter(user=request.user, event_id=event_id).delete()
#     return redirect('event_list')


from asyncio import events
from urllib import request
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Event, Registration
from datetime import date
from .models import Event


@login_required
def event_list(request):
    events = Event.objects.all()
    
    registered_event_ids = []
    if request.user.is_authenticated:
        registered_event_ids = Registration.objects.filter(user=request.user).values_list('event_id', flat=True)

    return render(request, 'event/event_list.html', {
        'events': events,
        'registered_event_ids': registered_event_ids,
    })

@login_required
def create_event(request):
    if request.method == 'POST':
        Event.objects.create(
            name=request.POST['name'],
            description=request.POST['description'],
            event_date=request.POST['event_date'],
            created_by=request.user
        )
        return redirect('event_list')
    return render(request, 'event/create_event.html')

@login_required
def register_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    Registration.objects.get_or_create(user=request.user, event=event)
    return redirect('event_list')

@login_required
def cancel_registration(request, event_id):
    Registration.objects.filter(user=request.user, event_id=event_id).delete()
    return redirect('event_list')

@login_required
def view_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    return render(request, 'event/view_event.html', {'event': event})

def home(request):
    return render(request, 'event/home.html')

def view_calendar(request):
    
    upcoming_events = Event.objects.filter(event_date__gte=date.today())
    return render(request, 'event/view_calendar.html', {'events': events})