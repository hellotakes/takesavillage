from django.contrib.auth.models import User
from django.db import models

from website.models.choices import Sex, Language, Speciality


class Specialist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    sex = models.CharField(max_length=1, choices=Sex.choices)

    profile_photo = models.ImageField(upload_to="specialist/profile/")

    physical = models.BooleanField(default=True)
    online = models.BooleanField(default=False)
    description = models.TextField(max_length=640)
    language = models.CharField(max_length=2, choices=Language.choices)
    speciality = models.CharField(max_length=128, choices=Speciality.choices)
    address = models.OneToOneField(
        'SpecialistAddress',
        on_delete=models.PROTECT
    )

    @property
    def first_name(self) -> str:
        return self.user.first_name

    @property
    def last_name(self) -> str:
        return self.user.last_name

    @property
    def email(self) -> str:
        return self.user.email

    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return f"{self.last_name} {self.first_name}"


class SpecialistAddress(models.Model):
    street = models.CharField(max_length=128)
    street_no = models.CharField(max_length=4)
    postal_code = models.IntegerField()
    city = models.CharField(max_length=128)
    country = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.street} {self.street_no}, {self.postal_code} {self.city}"

    def latitude(self) -> float:
        return 50.859589

    def longitude(self) -> float:
        return 4.351273
