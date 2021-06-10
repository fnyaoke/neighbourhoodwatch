from django.test import TestCase
from watch.models import *

# Create your tests here.
class NeighborhoodTestCase(TestCase):
    def test_user(self):
        self.assertTrue

    def test_save_user(self):
        self.assertTrue
    #Set up method

    def setUp(self):
        self.new_neighborhood = Neighborhood(name="neighborhood Name", location="your location")
        self.new_neighborhood.save()
        self.new_location = Neighborhood(neighborhood=self.new_neighborhood, occupants_count = "20", location="your location",admin="neighborhood admin")

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.new_neighborhood,Neighborhood))

    def test_save_method(self):
        self.new_neighborhood.save_neighborhood()
        neighborhood = Neighborhood.objects.all()
        self.assertTrue(len(neighborhood)>0)

    def test_delete_method(self):
        self.new_neighborhood.save_neighborhood()
        self.new_neighborhood.delete_neighborhood()
        neighborhood = Neighborhood.objects.all()
        self.assertTrue(len(neighborhood)==0)

class UserTestCase(TestCase):
    def test_user(self):
        self.assertTrue

    def test_save_user(self):
        self.assertTrue
    #Set up method

    def setUp(self):
        self.new_user = User(name="Your Name", email="youremail@domain.com", password="my password")
        self.new_user.save()
        self.new_neighborhood = User(user=self.new_user, email = "myemail@domain.com", neighborhood="your location")

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.new_user,User))

    def test_save_method(self):
        self.new_user.save_user()
        user = User.objects.all()
        self.assertTrue(len(user)>0)

    def test_delete_method(self):
        self.new_user.save_user()
        self.new_user.delete_user()
        user = User.objects.all()
        self.assertTrue(len(user)==0)