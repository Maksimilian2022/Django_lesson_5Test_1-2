from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)
class Sensor(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=60)

class Sensor_tempereture_data(models.Model):
    sensor_info_id = models.AutoField(primary_key=True)
    sensor_id = models.ForeignKey(Sensor, related_name="sensor_tempereture_data", on_delete=models.CASCADE)
    tempereture = models.FloatField(max_length=30)
    date_time = models.DateTimeField(max_length=60)
