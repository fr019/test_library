from datetime import datetime

from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from test_library.library.api.serializers import AuthorSerializer, BookSerializer, SubscriberSerializer
from test_library.library.models import Author, Book, Subscriber
from test_library.library.permissions import IsAdminUerOrIsAuthenticatedAndReadOnly


class AuthorViewSet(ModelViewSet):
    serializer_class = AuthorSerializer
    permission_classes = (IsAdminUerOrIsAuthenticatedAndReadOnly,)
    queryset = Author.objects.all()


class BookViewSet(ModelViewSet):
    serializer_class = BookSerializer
    permission_classes = (IsAdminUerOrIsAuthenticatedAndReadOnly,)
    queryset = Book.objects.all()

    def get_queryset(self, *args, **kwargs):
        if self.request.user.is_staff:
            return self.queryset
        else:
            return self.queryset.filter(publication_year__lte=datetime.now().year)


class SubscriberViewSet(ModelViewSet):
    serializer_class = SubscriberSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Subscriber.objects.all()
