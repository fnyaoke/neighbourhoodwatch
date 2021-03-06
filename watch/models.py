from django.db import models
from django.contrib import admin

# from django.contrib.auth.models import User

# Create your models here.

# STATUS_CHOICES = [
#     ('d', 'Draft'),
#     ('p', 'Published'),
#     ('w', 'Withdrawn'),
# ]
class Neighborhood(models.Model):
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=50)
    occupants_count = models.IntegerField
    # admin = models.ForeignKey(admin,blank=True,null=True)

    def __str__(self):
        return self.name

    def save_neighborhood(self):
      self.save()

    def delete_neighborhood(self):
      self.delete()

    @classmethod
    def find_neighborhood(cls, name):
      return cls.objects.filter(name_icontains=name)

    @classmethod
    def update_neighborhood(cls, id, name):
      update = cls.objects.filter(id=id).update(name=name)
      return update

    def make_published(modeladmin, request, queryset):
        queryset.update(status='p')


class User(models.Model):
    name = models.CharField(max_length=50)
    email = models. EmailField()
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE)

    def __str__(self):
      return self.name

    def save_user(self):
      self.save()

    def delete_user(self):
      self.delete()

class Business(models.Model):
    name=models.CharField(max_length=50)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    email=models.EmailField()
    neighborhood=models.ForeignKey(Neighborhood,on_delete=models.CASCADE)

    def __str__(self):
      return self.name

    def save_business(self):
      self.save()

    def delete_business(self):
      self.delete()

    @classmethod
    def find_business(cls, name):
      return cls.objects.filter(name_icontains=name)

    @classmethod
    def update_business(cls, id, name):
      update = cls.objects.filter(id=id).update(name=name)
      return update