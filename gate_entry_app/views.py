from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Person, AttendanceHistory
from django.contrib.auth.decorators import login_required


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
        hours = (a.exit_date-a.entry_date).total_seconds() / 3600
        hours_round = round(hours)
        attendance_list.append([a.entry_date.year, a.entry_date.month, a.entry_date.day, hours_round])
    context = {'person': person, 'attendance_list': attendance_list}
    return render(request, 'gate_entry_app/attendance_history.html', context)
