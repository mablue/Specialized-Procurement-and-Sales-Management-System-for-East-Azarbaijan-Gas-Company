from django.db import models


# Create your models here.


class Kala(models.Model):
    sharh = models.CharField(max_length=500, verbose_name="شرح")
    vahede_andazegiri = models.CharField(max_length=500, verbose_name="واحد کالا")
    mesc = models.CharField(max_length=500, verbose_name="شماره طبقه بندی کالا (MESC)")
    class Meta:
        verbose_name = "کالا"
        verbose_name_plural = "کالا ها"

    def __str__(self):
        return str(self.sharh)
