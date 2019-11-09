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


def search_results(request):
    if 'image' in request.GET and request.GET['image']:
        search_term = request.GET.get('image')
        searched_images = Image.search_by_category(search_term)
        message = f'{search_term}'

        return render(request, 'all-gallery/search.html', {'message': message, 'images': searched_images})

    else:
        message = 'There are no results. Enter a search query.'

        return render(request, 'all-gallery/search.html', {'message': message})
