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


class Hotel(models.Model):
    title = models.CharField(max_length=128)
    likes = models.PositiveIntegerField()
    dislikes = models.PositiveIntegerField()

    @property
    def residents(self):
        reservations = Reservation.objects.filter(room__in=self.rooms.all())
        return User.objects.filter(reservations__in=reservations).distinct()

    @property
    def free_room_for_today(self):
        return len(self.rooms.exclude(
            reservations__start__lte=datetime.now(),
            reservations__end__gte=datetime.now(),
        ))


class Room(models.Model):
    title = models.CharField(max_length=128)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='rooms')


class Reservation(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='reservations')
    start = models.DateField()
    end = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reservations')
