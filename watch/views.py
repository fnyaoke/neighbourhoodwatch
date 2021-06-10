from django.core.checks import messages
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import status
from django.http import Http404
from .models import *
from .serializers import *

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-neighborhood_id')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class NeighborhoodViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows neighborhood to be viewed or edited.
    """

    queryset = Neighborhood.objects.all()
    serializer_class = NeighborhoodSerializer
    permission_classes = [permissions.IsAuthenticated]


class BusinessViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows neighborhood to be viewed or edited.
    """
    queryset = Business.objects.all()
    serializer_class = BusinessSerializer
    permission_classes = [permissions.IsAuthenticated]

# list views

class NeighborhoodList(APIView):
  def get_neighborhood(self, pk):
    try:
        return Neighborhood.objects.get(pk=pk)
    except Neighborhood.DoesNotExist:
        return Http404()

  def get(self,request, format=None):
    neighborhood= Neighborhood.objects.all()
    serializers=NeighborhoodSerializer(neighborhood, many=True)
    return Response(serializers.data)

  def post(self,request,format=None):
    serializers=NeighborhoodSerializer(data=request.data)
    if serializers.is_valid():
      serializers.save()
      neighborhood=serializers.data
      response = {
          'data': {
              'neighborhood': dict(neighborhood),
              'status': 'success',
              'message': "neighborhood created successfully"
          }
      }
      return Response(response, status=status.HTTP_200_OK)
    return Response(serializers.errors , status= status.HTTP_400_BAD_REQUEST)


  def put(self, request, pk, format=None):
    neighborhood = self.get_neighborhood(pk=pk)
    serializers = NeighborhoodSerializer(neighborhood, request.data)
    if serializers.is_valid():
      serializers.save()
      neighborhood=serializers.data
      response = {
          'data': {
              'neighborhood': dict(neighborhood),
              'status': 'success',
              'message': "neighborhood updated successfully"
          }
      }
      return Response(response)
    else:
      return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, pk, format=None):
    neighborhood = self.get_neighborhood(pk)
    neighborhood.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

class BusinessList(APIView):

  def get_business(self, pk):
    try:
        return Business.objects.get(pk=pk)
    except Business.DoesNotExist:
        return Http404()


  def get(self, request,format=None):
    business=Business.objects.all()
    serializers=BusinessSerializer(business, many=True)
    return Response(serializers.data)


  def post(self, request, format=None):
    serializers=BusinessSerializer(data=request.data)
    if serializers.is_valid():
      serializers.save()
      business=serializers.data
      response = {
          'data': {
              'business': dict(business),
              'status': 'success',
              'message':"Business Created successfully",
          }
      }
      return Response(response, status=status.HTTP_200_OK)
    return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


  def put(self, request, pk, format=None):
    business = self.get_business()
    serializers = BusinessSerializer(business, request.data)
    if serializers.is_valid():
      serializers.save()
      business_list=serializers.data
      response = {
          'data': {
              'business': dict(business_list),
              'status': 'success',
              'message': "Business updated successfully",
          }
      }
      return Response(response)
    else:
      return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, pk, format=None):
    business = self.get_business()
    business.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

class UserList(APIView):

  def get_users(self,pk):
    try:
        return User.objects.get(pk=pk)
    except User.DoesNotExist:
        raise Http404()

  def get(self,request,format=None):
    users=User.objects.all()
    serializers=UserSerializer(users, many=True)
    return Response(serializers.data)

  def post(self, request, format=None):
    serializers=UserSerializer(data=request.data)
    if serializers.is_valid():
      serializers.save()

      users=serializers.data
      response={
        'data':{
          'users':dict(users),
          'status':'success',
          'message':"User created successfully",
        }
      }
      return Response(response, status=status.HTTP_200_OK)
    return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

  def put(self,request,pk,format=None):
    users=self.get_users(pk)
    serializers=UserSerializer(users,request.data)
    if serializers.is_valid():
      serializers.save()
      users_list=serializers.data
      response = {
          'data': {
              'users': dict(users_list),
              'status': 'success',
              'message': "User updated successfully"
          }
      }
      return Response(response, status=status.HTTP_200_OK)
    else:
      return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)

  def delete(self,request,pk,format=None):
    users=self.get_users()
    users.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

