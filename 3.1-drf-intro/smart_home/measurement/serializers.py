from rest_framework import serializers
from .models import Sensor, Sensor_tempereture_data
# TODO: опишите необходимые сериализаторы



class SensorSerializeAll(serializers.Serializer):
    name = serializers.CharField(max_length=30)
    description = serializers.CharField(max_length=60)


class SensorInfoSerialize(serializers.Serializer):
    class Meta:
        model = Sensor_tempereture_data
        fields = ('sensor_info_id', 'sensor_id', 'tempereture', 'date_time')

class SensorSerialize(serializers.Serializer):
    sensor_id = SensorInfoSerialize(many=True, read_only=True)
    id = serializers.IntegerField()
    name = serializers.CharField()
    description = serializers.CharField()
    class Meta:
        model = Sensor
        fields = ('id', 'name', 'description', 'sensor_id')

