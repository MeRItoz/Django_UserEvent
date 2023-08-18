# UserEvent/urls.py

from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter
from api.views import UserViewSet, EventViewSet, CollaboratorViewSet

# Create a router for the API views
router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'events', EventViewSet,  basename='event')
router.register(r'collaborators', CollaboratorViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),

]
