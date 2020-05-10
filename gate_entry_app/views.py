from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Person, AttendanceHistory, Role, Gate, Device
from django.contrib.auth.decorators import login_required
from .forms import EntryExitSimulationForm
from django.http import Http404
from datetime import datetime


@login_required
def people_list(request):
    people = Person.objects.all().order_by('first_name', 'last_name')
    return render(request, 'gate_entry_app/people_list.html', {'people': people})


@login_required
def attendance_history(request, pk):
    person = get_object_or_404(Person, pk=pk)
    attendance_data = AttendanceHistory.objects.filter(person=person)
    attendance_list = []
    for a in attendance_data:
        if a.exit_date and a.entry_date:
            hours = (a.exit_date-a.entry_date).total_seconds() / 3600
            hours_round = round(hours)
            attendance_list.append([a.entry_date.year, a.entry_date.month, a.entry_date.day, hours_round])
    context = {'person': person, 'attendance_list': attendance_list}
    return render(request, 'gate_entry_app/attendance_history.html', context)


@login_required
def entry_exit_simulation(request):
    form = EntryExitSimulationForm()
    form.fields['device'].choices = get_devices()
    form.fields['person'].choices = get_people()
    context = {'form': form}
    if request.method == 'POST':
        print('form is valid')
        person_id = request.POST.get('person')
        device_id = request.POST.get('device')
        date = request.POST.get('date')
        context['success'] = False
        date = datetime(*[int(v) for v in date.replace('T', '-').replace(':', '-').split('-')])
        current_tz = timezone.get_current_timezone()
        date = current_tz.localize(date)
        if is_access_allowed(person_id, device_id, date):
            context['success'] = True
    return render(request, 'gate_entry_app/entry_exit_simulation.html', context)


def is_access_allowed(person_id, device_id, date):
    try:
        person = get_object_or_404(Person, pk=person_id)
        device = get_object_or_404(Device, pk=device_id)
        role = get_object_or_404(Role, pk=person.role.id, gates=device.gate)
        print("Access is allowed")
        if device.gate.gate_name == 'Main gate':
            if device.is_entry_device:
                attendance_record = AttendanceHistory(person=person, gate=device.gate, entry_date=date, exit_date=None)
                attendance_record.save()
                print(attendance_record.entry_date)
            else:
                attendance_hist = AttendanceHistory.objects.filter(person=person, gate=device.gate)
                for att in attendance_hist:
                    if att.entry_date and att.exit_date is None and att.entry_date.year == date.year and\
                       att.entry_date.month == date.month and att.entry_date.day == date.day:
                        att.exit_date = date
                        att.save()
                        break
        return True
    except Http404:
        print("Access is not allowed")
        return False


def get_people():
    people = Person.objects.all().order_by('first_name', 'last_name')
    people_list = ((person.id, person.__str__()) for person in people)
    return people_list


def get_devices():
    devices = Device.objects.all()
    devices_list = ((device.id, device.__str__()) for device in devices)
    return devices_list
