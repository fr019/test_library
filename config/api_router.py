from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from test_library.library.api.views import AuthorViewSet, BookViewSet, SubscriberViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("authors", AuthorViewSet)
router.register("books", BookViewSet)
router.register("subscribers", SubscriberViewSet)


app_name = "api"
urlpatterns = router.urls
