from django.shortcuts import render


def people_list(request):
    return render(request, 'gate_entry_app/hello.html', {})
