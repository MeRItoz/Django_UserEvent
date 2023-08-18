# api/views.py

from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .models import User, Event, Collaborator
from .serializers import UserSerializer, EventSerializer, CollaboratorSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['creator']

class CollaboratorViewSet(viewsets.ModelViewSet):
    queryset = Collaborator.objects.all()
    serializer_class = CollaboratorSerializer
