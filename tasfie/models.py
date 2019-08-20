from django.db import models

# Create your models here.
from taghaza.models import Taghaza



class Tasfie(models.Model):
    taghaza = models.ForeignKey(Taghaza, on_delete=models.DO_NOTHING)
    bank = models.CharField(max_length=500, verbose_name="نام بانک",default="ملت")
    shomare = models.CharField(max_length=500, verbose_name="شماره تسویه")
    tarikh = models.DateField(verbose_name="تاریخ تسویه")
    mablagh = models.IntegerField(verbose_name="مبلغ تسویه")
    noe = models.IntegerField(verbose_name="نوع تسویه",choices=[
        (0,'تنخواه‌گردان'),
        (1,'ازمحل‌تقاضا'),
        (2,'علی‌الحساب'),

    ])
    


    class Meta:
        verbose_name = "تسویه"
        verbose_name_plural = "تسویه ها"
