#from django.shortcuts import render
# the above should be removed for creating custom api

from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API View"""
    # allows us to define the application logic for the endpoint we'll assign to this view
    # it chooses the right function based on the request
    # a URL will be assigned to the API

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


# Create your views here.
