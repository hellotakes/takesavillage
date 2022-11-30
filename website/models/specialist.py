from django.db import models

from website.models.choices import Sex, Language, Speciality


class Specialist(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    sex = models.CharField(max_length=1, choices=Sex.choices)

    profile_photo = models.ImageField(upload_to="specialists/profiles/")

    physical = models.BooleanField(default=True)
    online = models.BooleanField(default=False)
    description = models.TextField(max_length=640)
    language = models.CharField(max_length=2, choices=Language.choices)
    speciality = models.CharField(max_length=128, choices=Speciality.choices)
    address = models.OneToOneField(
        'SpecialistAddress',
        on_delete=models.PROTECT
    )


class SpecialistAddress(models.Model):
    street = models.CharField(max_length=128)
    street_no = models.PositiveSmallIntegerField()
    city = models.CharField(max_length=128)
    postal_code = models.PositiveSmallIntegerField()
    country = models.CharField(max_length=128)

