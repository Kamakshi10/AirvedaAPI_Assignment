from django.contrib import admin
from .models import devices ,humidityReading, temperatureReading

# registering models
admin.site.register(devices)
admin.site.register(humidityReading)
admin.site.register(temperatureReading)


