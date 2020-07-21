from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    '''allow user to edit only their own profile'''

    # gets called every time a request to the api we assigned the permission to
    # returns a true or false
    def has_object_permission(self, request, view, obj):
        '''check user is trying to edit their own profile'''

        # check if method made for request is in the safe_methods list
        # a safe method would be like GET because it doesn't make changes
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id
        # implicit "else" due to indentation
        # check if object being updated matches authenticated user profile
        # that is it checks the id

class UpdateOwnStatus(permissions.BasePermission):
    '''allows user to update only their own status'''

    def has_object_permission(self, request, view, obj):
        '''checks that he user is trying to update their own status'''
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user_profile.id==request.user.id 
        