# database faker shell
# run with this command in django shell:
# from chortke.populator import f

import random
from django.db.models.aggregates import Count
from random import randint
from faker import Faker
from aghlam.models import Aghlam
from factor.models import Factor
from kala.models import Kala
# from sefaresh.models import Sefaresh
from sherkat.models import Sherkat
from taghaza.models import Taghaza
# from pardaxt.models import Pardaxt


class f:
 
    def random(self):
        count = self.aggregate(count=Count('id'))['count']
        random_index = randint(0, count - 1)
        return self.all()[random_index]

    fake = Faker('fa_ir')

    tbl="taghaza"
    for _ in range(10):
        # print(Vahed.objects.filter(pk=fake.random_int(min=0, max=Vahed.objects.count()-1)).first())
        print(tbl+": "+str(_))
        new = Taghaza(
            vahed=fake.random_int(min=1,max=6,step=1),
            shomare=fake.random_int(min=1000000000, max=9999999999, step=1),
            tarikh=fake.date(),
            sharh=fake.random_element(elements=(
                'شیر ۲ اینچ',
                'لباس کار',
                'کنتور گاز',
                'لفتراک',
                'لیوان یکبارمصرف',
                'چای',
                'لوله چهار اینچ',
            )), )
        new.save()

    tbl="kala"
    for _ in range(10):
        print(tbl+": "+str(_))

        new = Kala(
            sharh=fake.random_element(elements=(
                'جعبه',
                'کاغذ ',
                'مداد',
                'خودکار',
                'جارو',
                'تخمه',
                'اتومبیل',
            )),
            vahede_andazegiri=fake.random_element(elements=(
                'عدد',
                'متر',
                'جعبه',
                'فوت',
                'اینچ',
                'کیلوگرم',
                'فروند',
            )), )
        new.save()

    tbl="sherkat"
    for _ in range(10):
        print(tbl+": "+str(_))
        new = Sherkat(
            nam="شرکت " + fake.name() +fake.random_element(elements=(" و شرکا","و برادران","")),
            tel=fake.random_int(min=10000000000, max=99999999999),
            mob=fake.random_int(min=10000000000, max=99999999999),
        )
        new.save()
    #
    # tbl="sefaresh"
    # for _ in range(10):
    #     print(tbl+": "+str(_))
    #     new = Sefaresh(
    #         taghaza=Taghaza.objects.order_by('?').first(),
    #         kala=Kala.objects.order_by('?').first(),
    #         meghdar=fake.random_int(min=1, max=100, step=1),
    #     )
    #     new.save()

    tbl="factor"
    for _ in range(10):
        print(tbl+": "+str(_))
        new = Factor(
            taghaza=Taghaza.objects.order_by('?').first(),
            shomare=fake.random_int(min=1000000000, max=9999999999, step=1),
            tarikh=fake.date(), # date_between_dates(date_start="-616y", date_end="-621y"),
            arzeshe_afzude=fake.random_element(elements=(True, False)),
        )
        new.save()

    tbl="ghalam"
    for _ in range(10):
        print(tbl+": "+str(_))
        new = Aghlam(
            factor=Factor.objects.order_by('?').first(),
            kala=Kala.objects.order_by('?').first(),
            sherkat=Sherkat.objects.order_by('?').first(),
            mablagh=fake.random_int(min=10000, max=100000, step=1),
            meghdar=fake.random_int(min=1, max=100, step=1),

        )
        new.save()

    # tbl="pardaxt"
    # for _ in range(10):
    #     print(tbl+": "+str(_))
    #     new = Pardaxt(
    #         fish = ,
    #         tarikh = fake.date_between_dates(date_start="-616y", date_end="-621y"),
    #         hesab = fake.random_int(min=1000000000000, max=9999999999999, step=1),
    #         name_bank = fake.random_element(elements=(
    #             'ملی',
    #             'ملت',
    #             'سپه',
    #             'پارسیان',
    #             'پاسارگاد',
    #             'جوانان خیر',
    #             'کشاورزی',
    #         )),
    #         elame_vajh = fake.random_int(min=1000000000, max=9999999999, step=1),
    #         factor = Factor.objects.order_by('?').first()
    #
    #     )
    #     new.save()
