# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
import datetime
from .models import Image, Category, Location

# Create your tests here.


class CategoryTestClass(TestCase):
    def setUp(self):
        self.techno = Category(category='techno')
        self.techno.save_category()

    def test_instance(self):
        self.assertTrue(isinstance(self.techno, Category))

    def tearDown(self):
        self.techno.delete_category()


class LocationTestClass(TestCase):
    def setUp(self):
        self.kigali = Location(location='kigali')
        self.kigali.save_location()

    def test_instance(self):
        self.assertTrue(isinstance(self.kigali, Location))

    def test_updating_location(self):
        location = Location.get_location_id(self.kigali.id)
        location.update_location('kigali')
        # location = Location.get_location_id(self.kigali.id)
        self.assertTrue(location.location == 'kigali')

    def tearDown(self):
        self.kigali.delete_location()
