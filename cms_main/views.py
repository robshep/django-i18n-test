from django.http import HttpResponse
from django.utils.translation import gettext_lazy as _
from django.utils.text import format_lazy
from django.shortcuts import render

ROCK_CANNONS = [
    {"id": 1, "name": "Gwaen Gynfi 1", "desc_en": "Large Rock", "desc_cy": "Cerrig Mawr"},
    {"id": 101, "name": "Lon Clegir", "desc_en": "Small Rock", "desc_cy": "Cerrig Back"},
    {"id": 201, "name": "Llyn Peris", "desc_en": "Nice Rock", "desc_cy": "Cerrig Iawn"},
]

ROCK_CANNONS_BY_ID = { rc['id']:rc for rc in ROCK_CANNONS }

def show_map(request):
    return render(request, 'map.html')

def show_about(request):
    return render(request, 'about.html')

def show_rc_list(request):
    return render(request, 'rc_list.html', {"list": ROCK_CANNONS})

def show_rc_detail(request, rc_id):
    rc = ROCK_CANNONS_BY_ID[rc_id]
    return render(request, 'rc_detail.html', {"rc": rc, "rc_id": rc_id})