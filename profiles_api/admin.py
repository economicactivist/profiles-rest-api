from django.contrib import admin
from profiles_api import models
# Register your models here.

admin.site.register(models.UserProfile)
# tells django to register model with admin interface so that is accessible
# you still have to add this line and "from profiles_api..." even though
# you ran python manage.py createsuperuser previously
admin.site.register(models.ProfileFeedItem)
