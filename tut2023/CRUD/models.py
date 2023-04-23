from django.db import models
from django.utils import timezone


class CRUD(models.Model):
  firstname = models.CharField(max_length=255,default='')
  lastname = models.CharField(max_length=255,default='')
  image = models.ImageField(upload_to='images',default='')

  def __str__(self):
    return self.firstname

class Pred(models.Model):
    fid = models.ForeignKey(CRUD, on_delete=models.CASCADE)
    prediction = models.CharField(max_length=255, default='')

    def __str__(self):
      return f"{self.fid.firstname} - {self.prediction}"

