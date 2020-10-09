from datetime import datetime

from django.core.validators import MaxValueValidator
from django.db import models

from test_library.users.models import User


class Book(models.Model):
    title = models.CharField('Title', max_length=255)
    language = models.CharField('Language', max_length=255)
    publication_year = models.IntegerField('Publication year',
                                           default=datetime.now().year,
                                           validators=[MaxValueValidator(9999)]
                                           )


class Author(models.Model):
    first_name = models.CharField('First name', max_length=255)
    middle_name = models.CharField('Middle name', max_length=255)
    last_name = models.CharField('Last name', max_length=255)


class Subscriber(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    @property
    def first_name(self):
        return self.user.first_name

    @property
    def middle_name(self):
        return self.user.middle_name

    @property
    def last_name(self):
        return self.user.last_name

    @property
    def email(self):
        return self.user.email
