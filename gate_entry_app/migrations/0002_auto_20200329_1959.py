# Generated by Django 3.0.4 on 2020-03-29 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gate_entry_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendancehistory',
            name='entry_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='attendancehistory',
            name='exit_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
