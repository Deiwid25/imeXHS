from django.db import models

class Element(models.Model):

  id = models.CharField(max_length=100, primary_key=True, editable=True)
  device_name = models.CharField(max_length=100)
  average_before_normalization = models.FloatField()
  average_after_normalization = models.FloatField()
  data_size = models.IntegerField()
  raw_data = models.JSONField()

  def __str__(self):
      return self.device_name
