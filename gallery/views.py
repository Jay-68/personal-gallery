# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Image
import datetime as dt
# Create your views here.


def welcome(request):
    return render(request, 'welcome.html')


def gallery_of_day(request):
    date = dt.date.today()
    gallery = Image.get_all_images()

    return render(request, 'all-gallery/today-gallery.html', {'date': date, 'gallery': gallery})

def