# from django.shortcuts import render
# the above should be removed for creating custom api

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
# list of useful http status codes that you can use when returning responses from your api
from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions


class HelloApiView(APIView):
    """Test API View"""
    # allows us to define the application logic for the endpoint we'll assign to this view
    # it chooses the right function based on the request
    # a URL will be assigned to the API

    serializer_class = serializers.HelloSerializer
    # whenever you're sending a post, put, or patch request expect an input of "name"
    # and we'll validate it at a max length of 10

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        # 'format' won't be used but it's best practice to include it
        an_apiview = [
            'Uses HTTP methods as functions (get, post, patch, put, delete)',
            'Is similar to a traditional Django View but built specifically for APIs',
            'Gives you the most control over application logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})

    def post(self, request):
        '''create a hello message with our name'''
        # retreive the serializer and pass in the data sent in the request

        serializer = self.serializer_class(data=request.data)
        # looks weird but it's the standard way to retrieve the serializer class
        # the (data=request.data) assigns the data from POST request to the API view
        # confusing need to research more (perhaps it extracts the data type)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})

        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
            # errors are automatically generated based on validation rules

    def put(self, request, pk=None):
        """handles updating an object"""
        # the pk= allows the method to know which field you want to update
        # other logic could be added in complex api
        return Response(dict(method='PUT'))

    def patch(self, request, pk=None):
        '''handles a partial update of an object'''
        return Response(dict(method='PATCH'))

    def delete(self, request, pk=None):
        '''deletes an object'''
        return Response(dict(method='DELETE'))


class HelloViewSet(viewsets.ViewSet):
    '''Test API ViewSet'''
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        '''return a hello message'''
        a_viewset = [
            'Uses actions (list, create, retireve, update partial_update)',
            'Automatically maps to URLs using Routers',
            'Provides more functionality with less code',
        ]
        return Response(dict(message='Hello', a_viewset=a_viewset))

    def create(self, request):
        '''create a new hello message(POST)'''
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response(dict(message=message))

        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        '''get a specific object based on id'''
        return Response(dict(http_method='GET'))

    def update(self, request, pk=None):
        return Response(dict(http_method='PUT'))

    def partial_update(self, request, pk=None):
        return Response(dict(http_method='PATCH'))

    def destroy(self, request, pk=None):
        return Response(dict(http_method='DELETE'))


class UserProfileViewSet(viewsets.ModelViewSet):
    '''Handles creating and updating profiles'''
    # connect it to a serializer class (just like regular viewset)
    # provide a query set to the Modelviewset so it knows which
    # objects in the data base are going to be managed

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    # provides all the standard functons (create, list, update, etc) using objects.all()
    authentication_classes = (TokenAuthentication, )
    # comma at end creates tuple
    permissions_classes = (permissions.UpdateOwnProfile, )
    # permissions are used for fine-grained authorization
# Create your views here.
