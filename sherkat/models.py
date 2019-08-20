from django.db import models


# Create your models here.
from django.utils.safestring import mark_safe


class Sherkat(models.Model):
    nam = models.CharField(max_length=500, verbose_name="نام شرکت")
    # image = models.ImageField(verbose_name="تصویر",upload_to="static/uploads/pic",null=True)
    tel = models.IntegerField(verbose_name="شماره تلفن",blank=True,null=True,)
    mob = models.IntegerField(verbose_name="شماره موبایل",blank=True,null=True,)


    def __str__(self):
        return self.nam

    def image_tag(self):
        return mark_safe( u'<img src="%s" />' % self.image)

    image_tag.short_description = 'Image'
    image_tag.allow_tags = True
    class Meta:
        verbose_name = "شرکت"
        verbose_name_plural = "شرکت ها"
