from django.urls import path, re_path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'neighbors', views.NeighborhoodViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'business', views.BusinessViewSet)


urlpatterns=[
  path('api/neighbors/',views.NeighborhoodList.as_view(),name='neighbor'),
  path('api/business/',views.BusinessList.as_view(),name='business'),
  path('api/users/',views.UserList.as_view(),name='users'),
  path('api/update/users/<int:pk>/',views.UserList.as_view(),name='update_users'),
  path('api/delete/users/<int:pk>/',views.UserList.as_view(),name='delete_users'),
  re_path('api/update/business/(?P<pk>[0-9]+)/',views.BusinessList.as_view(),name='update_business'),
  path('api/delete/business/<int:pk>/',views.BusinessList.as_view(),name='delete_business'),
  path('api/update/neighbors/<int:pk>/',views.NeighborhoodList.as_view(),name='update_neighbors'),
  re_path('api/delete/(?P<pk>[0-9]+)/',views.NeighborhoodList.as_view(),name='delete_neighbors')
]