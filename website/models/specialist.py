from django.contrib.gis.db.models import PointField, GeometryField
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

    @property
    def full_name(self) -> str:
        return f"{self.last_name} {self.first_name}"

    def __str__(self):
        return f"{self.last_name} {self.first_name}"


class SpecialistAddress(models.Model):
    street = models.CharField(max_length=128)
    street_no = models.CharField(max_length=4)
    postal_code = models.IntegerField(max_length=4)
    city = models.CharField(max_length=128)
    country = models.CharField(max_length=64)
    point = PointField()

    def __str__(self):
        return f"{self.street} {self.street_no}, {self.postal_code} {self.city}"

    def latitude(self) -> float:
        return self.point.y

    def longitude(self) -> float:
        return self.point.x
