from django.shortcuts import render
from rest_framework import generics
from .models import User, Note, Contact
from .serializers import UserSerializer, NoteSerializer, ContactSerializer


class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ContactListCreateView(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
