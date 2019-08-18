from django.db import models

# Create your models here.
from kala.models import Kala
from taghaza.models import Taghaza


class Sefaresh(models.Model):
    taghaza = models.ForeignKey(Taghaza, on_delete=models.DO_NOTHING , verbose_name="شماره تقاضا")
    kala = models.ForeignKey(Kala, on_delete=models.DO_NOTHING, verbose_name="نام کالا")
    meghdar = models.IntegerField(verbose_name="مقدار")

    class Meta:
        verbose_name = "سفارش"
        verbose_name_plural = "سفارش ها"

    def __str__(self):
        return str(self.kala) + " به مقدار: " + str(self.meghdar) +" "+ self.kala.vahede_andazegiri
