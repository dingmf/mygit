from django.contrib.auth.models import AbstractUser
from django.db import models
import random


# Create your models here.
# 构建我们的用户
class MyUser(AbstractUser):
    phone = models.CharField(
        max_length=20,
        verbose_name="手机号",
        unique=True
    )
    icon = models.ImageField(
        upload_to='icons',
        null=True
    )




class Person(models.Model):
    name = models.CharField(
        max_length=40,
    )


class Category(models.Model):
    name = models.CharField(
        max_length=20,
        verbose_name="分类名",
        db_column='c_name',
        unique=True
    )
    # db_column 是负责该字段的名字
    desc = models.TextField(
        max_length=1000,
        verbose_name="描述"
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = "category"  # 指定表的名字


class Goods(models.Model):
    name = models.CharField(
        max_length=100
    )
    price = models.FloatField()
    id_datetime = models.DateTimeField(
        auto_now_add=True,
        verbose_name="生产日期"
    )
    category = models.ForeignKey(
        Category,
        verbose_name="分类"
    )

    def __str__(self):
        return self.name


class IdCard(models.Model):
    num = models.CharField(
        max_length=18,
        verbose_name="身份证号"
    )
    unite = models.CharField(
        verbose_name="签发单位",
        max_length=30
    )


class PerSons(models.Model):
    name = models.CharField(
        max_length=20,
        verbose_name="名字"
    )
    sex = models.CharField(
        max_length=10,
        verbose_name="性别"
    )
    idcard = models.OneToOneField(
        IdCard,
        verbose_name="身份证",
        null=True
    )


class Author(models.Model):
    name = models.CharField(
        max_length=20
    )

class Book(models.Model):
    title = models.CharField(
        max_length=20
    )
    authors = models.ManyToManyField(
        Author
    )

class Team(models.Model):
    name = models.CharField(
        max_length=30,
        verbose_name="球队名字",
        db_index=True
    )
    country = models.CharField(
        max_length=30,
        verbose_name="所属国家"
    )
    def __str__(self):
        return self.name

class PlayerManager(models.Manager):
    def create_play(self):
        player = Player()
        player.name = "孙悟空" + str(random.randint(0,100))
        player.age = random.randrange(100)
        player.count = random.randrange(1000)
        player.team_id = 1
        player.save()
        return player


class Player(models.Model):
    name = models.CharField(
        verbose_name="名字",
        max_length=30
    )
    age = models.IntegerField(
        verbose_name="年龄"
    )
    count = models.IntegerField(
        verbose_name="火力输出"
    )
    team = models.ForeignKey(
        Team,
        verbose_name="所属球队",
        null=True
    )
    my_objects = models.Manager()
    my_objects_one = PlayerManager( )
    def __str__(self):
        return self.name































