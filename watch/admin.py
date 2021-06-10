from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Neighborhood)
admin.site.register(Business)
admin.site.register(User)

# #Action Admin

# def make_published(neighborhoodadmin, request, queryset):
#     queryset.update(status='p')
#     make_published.short_description = "Mark verified Neighborhoods published"

# class NeighborhoodAdmin(admin.ModelAdmin):
#     list_display = ['name', 'status']
#     ordering = ['name']
#     actions = [make_published]



# admin.site.register(Neighborhood, NeighborhoodAdmin)