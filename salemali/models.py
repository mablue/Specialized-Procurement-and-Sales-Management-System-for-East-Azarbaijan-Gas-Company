from django.db import models


# Create your models here.

# سال مالی
class Salemali(models.Model):
    sal = models.IntegerField(verbose_name="سال")
    arzeshe_afzude = models.IntegerField(verbose_name="درصد ارزش افزوده", default=0)
    nerkhe_tafkik = models.IntegerField(verbose_name='نرخ تفکیک معامله ها ', )
    # is_active = models.BooleanField(default=False, verbose_name="فعال")

    class Meta:
        verbose_name = "سال مالی"
        verbose_name_plural = "سال‌های مالی"
        # app_label = 'My APP name'

    def __str__(self):
        return "سال {} با ارزش افزوده {} و نرخ تفکیک {}".format(self.sal, self.arzeshe_afzude, self.nerkhe_tafkik)
