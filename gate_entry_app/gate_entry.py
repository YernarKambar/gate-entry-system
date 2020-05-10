import sqlite3
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Person, AttendanceHistory, Role, Gate


def is_access_allowed(person_id, gate_id):
    person = get_object_or_404(Person, pk=person_id)
    print(person)
    gate = get_object_or_404(Gate, pk=gate_id)
    print(gate)
    gate_exist = Role.objects.filter(pk=person.role.id, gate_id=gate_id)
    print(gate_exist)


is_access_allowed(1, 1)

