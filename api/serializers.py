from rest_framework import serializers
from .models import User, Note, Contact


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = "__all__"


class ContactSerializer(serializers.ModelSerializer):
    notes = NoteSerializer(many=True, required=False)

    class Meta:
        model = Contact
        fields = "__all__"
