from django.db import models


class Appointment(models.Model):
    specialist = models.ForeignKey("website.Specialist", on_delete=models.PROTECT)
    from_time = models.DateTimeField()
    duration = models.DurationField()
    booked_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.specialist.full_name}  {self.from_time}"
