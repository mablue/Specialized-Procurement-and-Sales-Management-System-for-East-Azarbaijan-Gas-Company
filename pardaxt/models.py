from django.db import models


# Create your models here.
from factor.models import Factor


class Pardaxt(models.Model):
    factor = models.ForeignKey(Factor, on_delete=models.DO_NOTHING, verbose_name="فاکتور")
    fish = models.IntegerField(verbose_name="شماره فیش")
    tarikh = models.DateField(auto_now=False, auto_now_add=False, verbose_name="تاریخ فیش", )  # default=jmodels.date.today())
    # tarikh = models.DateField(verbose_name="تاریخ فیش")
    hesab = models.CharField(max_length=500, verbose_name="شماره حساب")
    name_bank = models.CharField(max_length=100, verbose_name="نام بانک")
    elame_vajh = models.IntegerField(verbose_name="شماره نامه اعلام وجه")

    class Meta:
        verbose_name = "پرداخت"
        verbose_name_plural = "پرداخت ها"
    # def getSherkat(self):
    #     return self.factor.sherkat.nam

    def __str__(self):
        return str(self.fish)
