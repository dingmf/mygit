from django.db import models

# Create your models here.
class Humen(models.Model):
    name = models.CharField(
        max_length=20,
        verbose_name='人名'
    )
    age = models.IntegerField(
        verbose_name='年纪',
        default=1
    )
    sex = models.CharField(
        max_length=6,
        verbose_name='性别'
    )
    # 继承
    class Meta:
        abstract = True
    #     返回值
    def __str__(self):
        return self.name

class Stu(Humen):
    score = models.IntegerField(
        verbose_name='成绩'
    )

class Teacher(Humen):
    salary = models.IntegerField(
        verbose_name='薪资'
    )

    def get_base_msg(self):
        msg = '姓名:{t_name},年纪:{t_age}'.format(
            t_name=self.name,
            t_age=self.age
        )
        return msg

