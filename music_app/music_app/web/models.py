from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from music_app.web.validators import validate_only_letters_or_numbers


class Profile(models.Model):
    USERNAME_MIN_LEN = 2
    USERNAME_MAX_LEN = 15

    AGE_MIN_VALUE = 0

    username = models.CharField(
        max_length=USERNAME_MAX_LEN,
        validators=(
            MinLengthValidator(USERNAME_MIN_LEN),
            validate_only_letters_or_numbers,
        )
    )

    email = models.EmailField()

    age = models.IntegerField(
        null=True,
        blank=True,
        validators=(
            MinValueValidator(AGE_MIN_VALUE),
        )
    )


class Album(models.Model):
    NAME_MAX_LEN = 30
    ARTIST_MAX_LEN = 30
    GENRE_MAX_LEN = 30
    GENRE_CHOICES = [
        ("Pop Music", "Pop Music"),
        ("Jazz Music", "Jazz Music"),
        ("R&B Music", "R&B Music"),
        ("Rock Music", "Rock Music"),
        ("Country Music", "Country Music"),
        ("Dance Music", "Dance Music"),
        ("Hip Hop Music", "Hip Hop Music"),
        ("Other", "Other"),
    ]
    PRICE_MIN_VALUE = 0

    name = models.CharField(
        max_length=NAME_MAX_LEN,
        unique=True,
    )

    artist = models.CharField(
        max_length=ARTIST_MAX_LEN,
    )

    genre = models.CharField(
        max_length=GENRE_MAX_LEN,
        choices=GENRE_CHOICES,
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    image_url = models.URLField()

    price = models.FloatField(
        validators=(
            MinValueValidator(PRICE_MIN_VALUE),
        )
    )

    class Meta:
        ordering = ('name', 'price')
        # persistence in display-order
        # for better UX
