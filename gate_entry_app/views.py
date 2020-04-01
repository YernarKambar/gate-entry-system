from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Person
from django.contrib.auth.decorators import login_required


@login_required
def people_list(request):
    people = Person.objects.all().order_by('first_name', 'last_name')
    return render(request, 'gate_entry_app/people_list.html', {'people': people})


@login_required
def attendance_history(request, pk):
    person = get_object_or_404(Person, pk=pk)
    return render(request, 'gate_entry_app/attendance_history.html', {'person': person})
