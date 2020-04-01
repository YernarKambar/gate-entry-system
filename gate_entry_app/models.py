from django.conf import settings
from django.db import models
from django.utils import timezone


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    role = models.ForeignKey('Role', on_delete=models.CASCADE)

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)

    class Meta:
        verbose_name = "Person"
        verbose_name_plural = "People"


class Role(models.Model):
    role_name = models.CharField(max_length=30)
    gates = models.ManyToManyField('Gate')

    def __str__(self):
        return self.role_name


class Gate(models.Model):
    gate_name = models.CharField(max_length=30)

    def __str__(self):
        return self.gate_name


class AttendanceHistory(models.Model):
    person = models.ForeignKey('Person', on_delete=models.CASCADE)
    gate = models.ForeignKey('Gate', on_delete=models.CASCADE)
    entry_date = models.DateTimeField(blank=True, null=True)
    exit_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.person.__str__() + ' ' + str(self.person.id)

    def add_exit_date(self, exit_date=None):
        if exit_date:
            self.exit_date = exit_date
        else:
            self.exit_date = timezone.now()
        self.save()

    def add_entry_date(self, entry_date=None):
        if entry_date:
            self.entry_date = entry_date
        else:
            self.entry_date = timezone.now()
        self.save()

    class Meta:
        verbose_name = "Attendance history"
        verbose_name_plural = "Attendance history"
