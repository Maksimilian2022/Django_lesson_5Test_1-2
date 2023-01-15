# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view, APIView
from rest_framework.generics import ListAPIView
from .models import Sensor, Sensor_tempereture_data
from .serializers import SensorSerialize, SensorSerializeAll
from datetime import datetime

# @api_view(['GET'])
# def get_sensor(request):
#     sensor_database = Sensor.objects.all()
#     serializer_sensor = SensorSerialize(sensor_database, many=True)
#     return Response(serializer_sensor.data)

class Senser_control(APIView):
    def get(self, request):
        if request.GET['all'] == 'True':
            sensor_database = Sensor.objects.all()
            serialize_sensor = SensorSerializeAll(sensor_database, many=True)
            return Response(serialize_sensor.data)
        else:
            sensor_id = request.GET['id']
            sensor_database = Sensor.objects.get(id=sensor_id)
            serialize_sensor = SensorSerialize(sensor_database, many=False)
            return Response(serialize_sensor.data)

    def post(self, request):
        data = request.data
        serializer = SensorSerializeAll(data)
        new_sensor = Sensor(name=serializer.data.get('name'), description=serializer.data.get('description'))
        new_sensor.save()
        return Response("Сохранено")


    def patch(self, request):
        data = request.data
        sensor_id = data.get('id')
        new_description = data.get('description')
        Sensor.objects.filter(id=sensor_id).update(description=new_description)
        return Response('Значение изменено')

class Measurements(APIView):
    def post(self, request):
        data = request.data
        sensor_id = data.get('sensor')
        sensor_tempereture = data.get('temperature')
        time_now = datetime.now()
        new_description = Sensor_tempereture_data(sensor_id=sensor_id, tempereture=float(sensor_tempereture), date_time=str(time_now))
        new_description.save()

        return Response('Температура обновлена')


