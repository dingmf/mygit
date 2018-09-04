from django.db import models
# from tinymce.models import HTMLField
# Create your models here.

class Player(models.Model):
    name = models.CharField(
        max_length=30,
        verbose_name="书名"
    )
    desc = models.CharField(
        max_length=251,
        verbose_name="简介"
    )
    rate = models.FloatField(
        verbose_name="评分"
    )
    # extra = HTMLField(
    #     null=True
    # )

    # objects = models.Manager()
    def __str__(self):
        return self.name

    # extra = HTMLField

class Humen(models.Model):
    name = models.CharField(
        max_length=30,
        verbose_name="作者"
    )
    player = models.ForeignKey(
        Player,
        verbose_name="所著书籍"
    )





