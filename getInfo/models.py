from django.db import models

# Create your models here.

# class Station(models.Model):
#     id_state = models.IntegerField(default=1)
#     name_state = models.CharField(max_length=200)
#     name_station = models.CharField(max_length=200)
#     id_wmo = models.IntegerField()
#     lat_num = models.FloatField()
#     lon_num = models.FloatField()
#     category_name = models.CharField(max_length=200)
#     category_id = models.IntegerField(default=1)
#     category_type = models.CharField(max_length=200)
#     name_city = models.CharField(max_length=200)
#     def __str__(self):
#         return self.name_station

class GetDataSynop_main(models.Model):
    is_active = models.IntegerField(default=1)
    period_visitor = models.CharField(max_length=100)
    date_visit = models.DateTimeField(auto_now_add=True)
    period_thermometer = models.IntegerField(default=0)
    period_screen_box = models.IntegerField(default=0)
    period_rain_gauge = models.IntegerField(default=0)
    period_rain_gauge_siphon = models.IntegerField(default=0)
    period_sundial = models.IntegerField(default=0)
    period_evaporation_pan = models.IntegerField(default=0)
    period_sensors = models.IntegerField(default=0)
    period_data_logger_panel = models.IntegerField(default=0)
    period_infrastructure = models.IntegerField(default=0)
    calibration_traditional_mercury_press_gauge = models.IntegerField(default=0)
    calibration_traditional_wind_speed = models.IntegerField(default=0)
    calibration_traditional_wind_direction = models.IntegerField(default=0)
    calibration_traditional_digital_press_gauge = models.IntegerField(default=0)
    calibration_traditional_radiation = models.IntegerField(default=0)
    calibration_automatic_pressure = models.IntegerField(default=0)
    calibration_automatic_tem_hum = models.IntegerField(default=0)
    calibration_automatic_radiation = models.IntegerField(default=0)
    seconder = models.CharField(max_length=100)
    seconder_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.is_active



