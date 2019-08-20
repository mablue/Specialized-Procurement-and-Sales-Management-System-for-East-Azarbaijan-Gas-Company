from django.db import models


# Create your models here.


class Kala(models.Model):
    # noe = models.CharField(max_length=500, verbose_name="نوع",null=True,blank=True,)
    sharh = models.CharField(max_length=500, verbose_name="شرح کالا",null=True,blank=True,)    
    # abead = models.CharField(max_length=500, verbose_name="ابعاد",null=True,blank=True,)
    # shekl = models.CharField(max_length=500, verbose_name="شکل",null=True,blank=True,)
    # rang = models.CharField(max_length=500, verbose_name="رنگ",null=True,blank=True,)
    # estefade = models.CharField(max_length=500, verbose_name="مورد استفاده",null=True,blank=True,)
    # jens = models.CharField(max_length=500, verbose_name="جنس",null=True,blank=True,)
    vahede_andazegiri = models.CharField(max_length=500, verbose_name="واحد کالا")
    mesc = models.CharField(max_length=500, verbose_name="شماره طبقه بندی کالا (MESC)")
    class Meta:
        verbose_name = "کالا"
        verbose_name_plural = "کالا ها"

    def __str__(self):
        return str(self.sharh)
