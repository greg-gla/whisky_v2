from django.test import TestCase
from pages.models import Distillery,Whisky
from django.urls import reverse

# Create your tests here.
class DistilleryMethodTests(TestCase):
    def test_Distillery_can_insert_data_successfully(self):
        distillery = Distillery(name = "testDist")
        distillery.save()

        self.assertEqual((distillery.name == "testDist"),True)

    def test_Distillery_data_can_be_edit_successfully(self):
         dist = Distillery.objects.get_or_create(name="testDist")[0]
         dist.name = "testDist_changeName"
         dist.save()

         self.assertEqual((dist.name == "testDist_changeName"),True)

    def test_Distillery_data_can_be_delete_successfully(self):
        dist = Distillery.objects.get_or_create(name="testDist")[0]
        dist.save()

        delete = dist.delete()
        self.assertEqual((delete[0] == 1),True)

class WhiskyMethodTests(TestCase):
    def test_Whisky_can_insert_data_successfully(self):
        dist = Distillery.objects.get_or_create(name="testDist_test_whisky")[0]
        whisky = Whisky(name = "whisky001",distillery = dist)
        whisky.save()

        self.assertEqual((whisky.name == "whisky001"),True)

    def test_Whisky_data_can_be_edit_successfully(self):
        dist = Distillery.objects.get_or_create(name="testDist_test_whisky")[0]
        whisky = Whisky(name = "whisky001",distillery = dist)
        whisky.save()
        whisky.name =  "whisky001_Edit"
        whisky.save()

        self.assertEqual((whisky.name == "whisky001_Edit"),True)

    def test_Whisky_data_can_be_delete_successfully(self):
        dist = Distillery.objects.get_or_create(name="testDist_test_whisky")[0]
        whisky = Whisky(name = "whisky001",distillery = dist)
        whisky.save()

        delete = whisky.delete()
        self.assertEqual((delete[0] == 1),True)

class AboutViewTests(TestCase):
    def test_about_view_is_valid(self):
        response = self.client.get(reverse('pages:about'))

        self.assertEqual(response.status_code, 200)