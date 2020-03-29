from django.contrib import admin
from .models import Person, Role, Gate, AttendanceHistory

# password superuser - qwe
admin.site.register([Person, Role, Gate, AttendanceHistory])
