from django.db import models
import locale

# Create your models here.
from kala.models import Kala
from sherkat.models import Sherkat
from taghaza.models import Taghaza
from django.conf import settings


class Aghlam(models.Model):
    taghaza = models.ForeignKey(Taghaza, related_query_name='taghaza', on_delete=models.DO_NOTHING,
                                verbose_name="تقاضا")
    # factor = models.ForeignKey(Factor, on_delete=models.CASCADE, verbose_name="فاکتور", null=True, blank=True, )
    kala = models.ForeignKey(Kala, on_delete=models.DO_NOTHING, verbose_name="نام کالا")
    sherkat = models.ForeignKey(Sherkat, on_delete=models.DO_NOTHING, verbose_name="تامین کننده", null=True, blank=True, )
    mablagh = models.IntegerField(verbose_name="مبلغ واحد", null=True, blank=True, )
    meghdar = models.IntegerField(verbose_name="مقدار", null=True, blank=True,)
    external = models.BooleanField(verbose_name="خارجی", default=False)

    class Meta:
        verbose_name = "قلم"
        verbose_name_plural = "اقلام"

    def __str__(self):
        star = ""
        # return str(self.kala.sharh) + "|" + str(self.meghdar)+  " " + str(self.kala.vahede_andazegiri) + "|به شماره تقاضای: "+str(self.taghaza)
        if len(self.factor_set.all())!=0 :
            star = "شماره فاکتور:" + str(self.factor_set.all().first())
            # star = '-'.join([str(i) for i in self.factor_set.all()])
        return "["+str(str(self.pk) +"]["+\
            str(self.kala.sharh)  +"]["+\
            str(self.meghdar)+str(self.kala.vahede_andazegiri) +"]["+\
            "قیمت واحد:"+str(self.mablagh)+ "ریال"+"]["+\
            "مبلغ کل:" + self.mablaghe_koll_splited()).replace('None',"0")+ "ریال"+"]["+\
            star+"][" + \
            "شماره تقاضا:" + str(self.taghaza) + "]"


    def mablaghe_koll_splited(self):
        try:
            tot = self.meghdar * self.mablagh
        except:
            tot = 0
        return '{:0,.0f}'.format(tot)
        # locale.setlocale(locale.LC_ALL, 'fa')
        # return locale.currency(tot, grouping=True)
    mablaghe_koll_splited.short_description = "مبلغ کل"

    def mablaghe_koll(self):
        return int(filter(str.isdigit, self.mablaghe_koll_splited(self)))


