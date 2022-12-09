from django.db import models

class File(models.Model):
  file = models.FileField(blank=False, null=False)
  timestamp = models.DateTimeField(auto_now_add=True)

class TenderImport(models.Model):
  CustomerRefNo = models.CharField(max_length = 50, null=True, blank=True)
  Refno = models.CharField(max_length = 50, null=True, blank=True)
  DESCRIPTION = models.TextField(null=True, blank=True)
  Image = models.BinaryField(null=True, blank=True)
  UNIT = models.CharField(max_length = 50, null=True, blank=True)
  Quantity = models.IntegerField(null=True, blank=True)
  Rate = models.FloatField(null=True, blank=True)
  Amount = models.FloatField(null=True, blank=True)
