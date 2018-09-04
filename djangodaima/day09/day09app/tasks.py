from celery import task
from django.core.mail import send_mail
from django.conf import settings
import time

@task
def first_task(loopnum):
    # 模拟一个耗时操作
    for i in range(loopnum):
        time.sleep(1)
        print("睡后1万元")

@task
def send_email(email):
    title = "邮件的标题"
    msg = "这个是异步"
    from_email = settings.DEFAULT_FROM_EMAIL
    recievers = [email, ]
    send_mail(
        title,
        msg,
        from_email,
        recievers,
        fail_silently=True,
    )
