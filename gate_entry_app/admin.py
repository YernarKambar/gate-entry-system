from django.contrib import admin
from .models import Person, Role, Gate, AttendanceHistory, Device

# password superuser - qwe
admin.site.register([Person, Role, Gate, AttendanceHistory, Device])
