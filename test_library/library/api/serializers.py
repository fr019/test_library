from django.contrib.auth import get_user_model
from rest_framework import serializers

from test_library.library.models import Author, Book, Subscriber

User = get_user_model()


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"


class SubscriberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriber
        fields = ("id", "first_name", "middle_name", "last_name", "email")
