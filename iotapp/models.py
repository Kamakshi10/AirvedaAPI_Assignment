from django.db import models
from django.utils import timezone

# stores information about devices
class devices(models.Model):
	uid=models.IntegerField()
	name=models.CharField(max_length=100)

	def __str__(self):
		return self.name

# temperature readings of all devices
class temperatureReading(models.Model):
	temperature=models.IntegerField()
	date=models.DateTimeField(default=timezone.now)
	device_id=models.ForeignKey(devices, on_delete=models.CASCADE)


# humidity readings off all devices
class humidityReading(models.Model):
	humidity=models.IntegerField()
	date=models.DateTimeField(default=timezone.now)
	device_id=models.ForeignKey(devices, on_delete=models.CASCADE)	

	