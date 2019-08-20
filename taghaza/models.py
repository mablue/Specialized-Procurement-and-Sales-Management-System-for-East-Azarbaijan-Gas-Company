import locale

from django.db import models
from django.utils.safestring import mark_safe

class Taghaza(models.Model):
    vahedHa = [
        
        (0, 'امورقراردادهاوپیمانکاران'),
        (1, 'بهره‌برداری'),
        (2, 'امور رفاهی'),
        (3, 'اندازه‌گیری و توزیع گاز'),
        (4, 'حراست'),
        (5, 'خدمات طرح‌ها'),
        (6, 'گازرسانی صنایع'),
        (7, 'فناوری اطلاعات'),
        (8, 'امورتدارکات وعملیات کالا'),
        (9, 'HSE اچ اس ای'),
        (10, 'روابط عمومی'),
        (11, 'امور ورزشی'),
        (12, 'سایر واحدهای ستادی'),

    ]

    # def FileNameHandler(self):
    #     return str(self.shomare)


    # name = models.CharField(max_length=500, unique=True)
    # parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    shomare = models.CharField(verbose_name="شماره تقاضا", max_length=500, unique=True)
    tarikh = models.DateField(auto_now=False, auto_now_add=False, verbose_name="تاریخ تقاضا")
    sharh = models.CharField(max_length=500, null=True, verbose_name="شرح تقاضا")
    baravord = models.IntegerField(null=True, verbose_name="مبلغ براورد اولیه")
    vahed = models.IntegerField(
        verbose_name="واحد متقاضی",
        choices=vahedHa,
    )

    def user_directory_path(instance, filename):
        return 'static/pics/taghaza/{0}/{1}'.format(instance.shomare,filename)
    image = models.ImageField(verbose_name="تصویر فرم تقاضای کالا (MT26)",upload_to = user_directory_path,default='static/pics/no-pic.jpg')


    class Meta:
        verbose_name = "تقاضا"
        verbose_name_plural = "تقاضا ها"
        # app_label = 'My APP name'

    def __str__(self):
        return str(self.shomare)  # + ": " + self.sharh

    def image_tag(self):
        return mark_safe(u'<style>#imgZoom{transition: transform .25s ease;border:1px solid orange;}#imgZoom:hover {transform:rotate(90deg) scale(16,25);position: absolute;z-index:1000;border:0.1px solid lightblue;}"</style><a target="_blank"  href="/%s"><img id="imgZoom" height="20px" width="20px" src="/%s" /></a>'% (self.image,self.image))

    image_tag.short_description = 'تصویر'
    image_tag.allow_tags = True


  

    def price(self):
        # factors = self.factor_set.all()
        # total = 0
        # for factor in factors:
        #     aghlam = factor.aghlam_set.all()
        #     for ghalam in aghlam:
        #         try:
        #             total += ghalam.mablagh * ghalam.meghdar
        #         except:
        #             total += 0
        total = 0
        aghlam = self.aghlam_set.all()
        for ghalam in aghlam:
                try:
                    total += ghalam.mablagh * ghalam.meghdar
                except:
                    total += 0
        return round(total,0)

    price.short_description = "مبلغ کل"

    def count(self):
        # factors = self.factor_set.all()
        # total = 0
        # for factor in factors:
        #     aghlam = factor.aghlam_set.all()
        #     for ghalam in aghlam:
        #         total += ghalam.meghdar
        # return total


        total = 0
        aghlam = self.aghlam_set.all()
        for ghalam in aghlam:
            try:
                total += ghalam.meghdar
            except:
                total += 0
        return total



    count.short_description = "تعداد قلم"
