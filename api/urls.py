
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, EventViewSet, CollaboratorViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'events', EventViewSet)
router.register(r'collaborators', CollaboratorViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
