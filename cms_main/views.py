from django.http import HttpResponse
from django.utils.translation import gettext_lazy as _
from django.utils.text import format_lazy
from django.shortcuts import render

from .models import Rock

def show_map(request):
    return render(request, 'map.html')

def show_about(request):
    return render(request, 'about.html')

def show_rc_list(request):
    return render(request, 'rc_list.html', {"list": Rock.objects.all()})

def show_rc_detail(request, rc_id):
    rc = Rock.objects.get(id=rc_id)
    return render(request, 'rc_detail.html', {"rc": rc, "rc_id": rc_id})