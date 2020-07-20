from django.urls import path, include
# use 'include' because we're using viewsets
from rest_framework.routers import DefaultRouter
from profiles_api import views

router = DefaultRouter()

router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')
# register specific viewsets with our router
# no need to add a '/' after 'hello-viewset'
router.register('profile', views.UserProfileViewSet)
# no need to specify 'base_name' because you have a queryset and DRF can
# figure out the base_name from the query set


urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
    path('', include(router.urls))  # for viewsets
]
