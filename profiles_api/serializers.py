# a serializer converts data inputs into python objects
# it's from the Django REST framework
# relates to POSTs, PUTs, and PATCHes
# are similar to django forms
# serializers can be used for validations (making sure correct data type is used)

from rest_framework import serializers
from profiles_api import models


class HelloSerializer(serializers.Serializer):
    # "Serializer" class name so it gets a capital "S"
    # define fields
    '''Serializes a name field for testing our APIView'''
    name = serializers.CharField(max_length=10)
##testing

class UserProfileSerializer(serializers.ModelSerializer):
    '''serializers a user profile object'''
    # MoldelSerializer allows you to use a Meta class to point to a specific
    # model in your project

    class Meta:
        model = models.UserProfile
        # sets serializer to point to userprofile model
        # list all fields you want to make accessible in api
        # or use field to create new models with serializer
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = dict(
            password=dict(
                write_only=True,
                style=dict(
                    input_type='password'
                )))

    def create(self, validated_data):
        '''create and return a new user'''
        # use createuser function instead of create function
        # allows allows password to be hashed
        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )
        # create and return new user from userprofile model manager
        return user

    def update(self, instance, validated_data):
        """Handle updating user account"""
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)
        # pop the unhashed password fron the dictionary and then hash it
        return super().update(instance, validated_data)
        # pass value up to the existing DRF update() method

class ProfileFeedItemSerializer(serializers.ModelSerializer):
    '''Serializes profile feed items'''
    class Meta:
        model = models.ProfileFeedItem
        fields = ('id', 'user_profile', 'status_text', 'created_on')
        extra_kwargs = dict(user_profile=dict(read_only=True))
        #make user profile field read only so that a user can't assign a 
        #feed item to another user 
