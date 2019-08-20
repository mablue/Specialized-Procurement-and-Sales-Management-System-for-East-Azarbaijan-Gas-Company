from django.db import models
from taghaza.models import Taghaza
from aghlam.models import Aghlam
from django.utils.safestring import mark_safe

class Factor(models.Model):
    taghaza = models.ForeignKey(Taghaza, on_delete=models.DO_NOTHING, verbose_name="تقاضا")


    aghlam = models.ManyToManyField(Aghlam, verbose_name="اقلام خریداری شده",)
    shomare = models.CharField(verbose_name="شماره فاکتور", null=True, max_length=500, unique=True )
    tarikh = models.DateField(auto_now=False, auto_now_add=False, verbose_name="تاریخ فاکتور",)
    arzeshe_afzude = models.BooleanField(default=True, verbose_name="ارزش افزوده")
    
    def user_directory_path(instance, filename):
        return 'static/pics/factor/{0}/{1}'.format(instance.shomare,filename)
    image = models.ImageField(verbose_name="تصویر فاکتور خرید",upload_to = user_directory_path,default='static/pics/no-pic.jpg')


    # sherkats = models.ForeignKey(Sherkat, on_delete=models.DO_NOTHING, verbose_name="فاکتور")

    class Meta:
        verbose_name = "فاکتور"
        verbose_name_plural = "فاکتور ها"

    def __str__(self):
        return str(self.shomare)

    def salemali(self):
        return self.tarikh.year

    salemali.short_description = "سال مالی"

    def image_tag(self):
        return mark_safe(u'<style>#imgZoom{transition: transform .25s ease;border:1px solid orange;}#imgZoom:hover {transform:  rotate(90deg) scaleX(16) scaleY(25);position: absolute;z-index:1000;border:0.1px solid lightblue;}"</style><a target="_blank"  href="/%s"><img id="imgZoom" height="20px" width="20px" src="/%s" /></a>'% (self.image,self.image))

    image_tag.short_description = 'تصویر'
    image_tag.allow_tags = True




    # def save(self, *args, **kwargs):
    #     if Factor.objects.get(taghaza=self.shomare).exists():
    #         pass
    #     else


    #     super(Taghaza, self).save(*args, **kwargs)



    #     if getattr(self, '_image_changed', True):
    #         small=rescale_image(self.image,width=100,height=100)
    #         self.image_small=SimpleUploadedFile(name,small_pic)
    #     super(Model, self).save(*args, **kwargs)

    def meghdar(self):
        return sum(i[0] for i in self.aghlam.all().values_list("meghdar"))

    def price(self):
        maghadir = ()
        for i in self.aghlam.all().values_list("meghdar"):
            maghadir += i
        mabalegh = ()
        for i in self.aghlam.all().values_list("mablagh"):
            mabalegh += i
        try:
            total = [a * b for a, b in zip(mabalegh, maghadir)]
        except:
            total = ()
        sumTot =  sum(total)
        import locale

        # locale.setlocale(locale.LC_ALL, 'fa')
        return '{:0,.0f}'.format(sumTot)
