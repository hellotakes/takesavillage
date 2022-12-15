from django.db import models

from website.models.choices import WeekDays


class CaregiverConsultationSlot(models.Model):
    specialist = models.ForeignKey("website.Caregiver", on_delete=models.PROTECT)
    parent = models.ForeignKey("website.Parent", on_delete=models.PROTECT)

    week_day = models.CharField(max_length=60, choices=WeekDays.choices)
    start = models.TimeField()
    end = models.TimeField()

    def __str__(self):
        return f"{self.specialist}  {self.week_day}: {self.start} -> {self.end}"
