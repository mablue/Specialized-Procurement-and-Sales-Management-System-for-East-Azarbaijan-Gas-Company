from django.db import models

# Create your models here.
from taghaza.models import Taghaza



class Resid(models.Model):
    taghaza = models.ForeignKey(Taghaza, on_delete=models.DO_NOTHING, verbose_name="تقاضا")
    tarikh = models.DateField(verbose_name="تاریخ رسید",null=True)
    shomare = models.CharField(verbose_name="شماره رسید",null=True,max_length=500,)


    def __str__(self):
        return str(self.shomare)# + ": " + self.sharh


    
    class Meta:
        verbose_name = "رسید"
        verbose_name_plural = "رسید ها"
