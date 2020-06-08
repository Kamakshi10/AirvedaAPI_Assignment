from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import devices, temperatureReading as tempRead, humidityReading as humidRead
from .serializers import deviceSerializer,temperatureReadingSerializer, humidityReadingSerializer
import dateutil.parser


def homeView(request):
	return render(request,'home.html')


#API to list all devices
@api_view(['GET'])
def list(request):
	data_val=devices.objects.all()
	serializer=deviceSerializer(data_val, many=True)
	return Response(serializer.data)



#API to retrieve a device
@api_view(['GET'])
def retrieve(request,pk):
	data_val=devices.objects.get(uid=pk)
	serializer=deviceSerializer(data_val, many=False)
	return Response(serializer.data)



#API to create a device 
@api_view(['POST'])
def create(request):
	serializer=deviceSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)



#API to delete a device	
@api_view(['DELETE'])
def delete(request,pk):
	data_val=devices.objects.get(uid=pk)
	data_val.delete()
	return Response('Device successfully deleted');



#API to retrieve readings of a device 
@api_view(['GET'])
def retrieve_readings(request,pk,parameter,starton,endon):
	start_date=dateutil.parser.parse(starton)
	end_date=dateutil.parser.parse(endon)

	if parameter=='temperature':
		data_val=tempRead.objects.filter(device_id__uid=pk,date__range=(start_date, end_date))
		serializer=temperatureReadingSerializer(data_val, many=True)
		
	elif parameter=='humidity':
		data_val=humidRead.objects.filter(device_id__uid=pk,date__range=(start_date, end_date))
		serializer= humidityReadingSerializer(data_val, many=True)
		
	return Response(serializer.data)