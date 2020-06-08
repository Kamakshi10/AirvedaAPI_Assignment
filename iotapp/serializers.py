from rest_framework import serializers
from .models import devices ,temperatureReading, humidityReading

class deviceSerializer(serializers.ModelSerializer):

	class Meta:
		model=devices
		fields='__all__'

class temperatureReadingSerializer(serializers.ModelSerializer):

	class Meta:
		model=temperatureReading
		fields='__all__'

class  humidityReadingSerializer(serializers.ModelSerializer):

	class Meta:
		model=humidityReading
		fields='__all__'