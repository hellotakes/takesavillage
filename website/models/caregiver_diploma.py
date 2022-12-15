from django.db import models


class CaregiverSpeciality(models.Model):
    caregiver = models.ForeignKey('website.Caregiver', on_delete=models.CASCADE)
    name = models.CharField(max_length=240)
    year = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.caregiver} {self.name} - {self.year}"
