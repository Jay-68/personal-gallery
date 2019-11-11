from django.test import TestCase
from .models import location, Category, Image


# Create your tests here.

class locationTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.location = location(location='Kibra')

    def tearDown(self):

        location.objects.all().delete()

    # Testing instance

    def test_instances(self):
        self.assertTrue(isinstance(self.location, location))

    # Test for saving method
    def test_save_location(self):
        self.location.save_location()
        locations = location.objects.all()
        self.assertFalse(len(locations) > 0)

    # Test for updating location
    def test_update_location(self):
        new_location = 'Compton'
        self.location.update_location(self.location.id, new_location)
        updated_location = location.objects.filter(location='Compton')
        self.assertFalse(len(updated_location) > 0)

    def test_delete_location(self):
        self.location.delete_location()
        location = location.objects.all()
        self.assertTrue(len(location) == 0)


class CategoryTestClass(TestCase):
    def setUp(self):
        self.category = Category(category_name='creativity')

    def tearDown(self):

        Category.objects.all().delete()

    # Testing instance
    def test_instances(self):
        self.assertTrue(isinstance(self.category, Category))

     # Test for saving method
    def test_save_category(self):
        self.category.save_category()
        categories = Category.objects.all()
        self.assertFalse(len(categories) > 0)

    # Test for updating category

    def test_update_category(self):
        new_category_name = 'Art'
        self.category.update_category(self.category.id, new_category_name)
        updated_category = Category.objects.filter(category_name='Art')
        self.assertFalse(len(updated_category) > 0)

    # Test for deleting category

    def test_delete_category(self):
        self.category.delete_category()
        category = Category.objects.all()
        self.assertTrue(len(category) == 0)


class ImageTestClass(TestCase):
    def setUp(self):
        self.location = location(location='kibra')
        self.location.save()

        self.category = Category(category_name='creativity')
        self.category.save()

        self.image_test = Image(image_name='image_test', image_description='This is a test image',
                                location=self.location, category=self.category)

    def test_inastance(self):
        self.assertTrue(isinstance(self.image_test, Image))

    def tearDown(self):
        Image.objects.all().delete()
        location.objects.all().delete()
        Category.objects.all().delete()

    def test_save_image(self):
        self.image_test.save_image()
        images = Image.objects.all()
        self.assertFalse(len(images) > 0)

    def test_update_image(self):

        self.image_test.save_image()
        self.image_test.update_image(
            self.image_test.id, 'media/test_image.jpg')
        updated_image = Image.objects.filter(image='media/test_image.jpg')
        self.assertFalse(len(updated_image) > 0)

    def test_delete_image(self):
        self.image_test.delete_image()
        images = Image.objects.all()
        self.assertTrue(len(images) == 0)