from rest_framework import serializers
from .models import User, Note, Contact


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "first_name", "last_name", "email", "phone_number"]


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ["date", "note"]


class ContactSerializer(serializers.ModelSerializer):
    notes = NoteSerializer(many=True, required=False)

    class Meta:
        model = Contact
        fields = [
            "id",
            "first_name",
            "last_name",
            "email",
            "social_media",
            "company",
            "phone_number",
            "job_title",
            "notes",
        ]

    def create(self, validated_data):
        notes_data = validated_data.pop("notes", [])

        contact = Contact.objects.create(**validated_data)

        for note_data in notes_data:
            note = Note.objects.create(contact=contact, **note_data)
            contact.notes.add(note)

        return contact

    def update(self, instance, validated_data):
        notes_data = validated_data.pop("notes", [])

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        for note_data in notes_data:
            note, created = Note.objects.update_or_create(
                contact=instance, defaults=note_data
            )
            instance.notes.add(note)

        instance.save()
        return instance
