from django.core.mail import send_mail
from django.template import loader
from django.conf import settings
import uuid
import hashlib

# 生成验证url host 是我们的域名
def get_verify_url(host):
    uuid_val = uuid.uuid4()
    uuid_str = str(uuid_val).encode("utf-8")
    md5 = hashlib.md5()
    md5.update(uuid_str)
    md5_str = md5.hexdigest()
    url = "http://{host}/axf/api/v1/active/{token}".format(
        host=host,
        token = md5_str
    )
    return [url, md5_str]

def send_verify_mail(email, host):
    res = get_verify_url(host)
    url = res[0]
    token = res[1]
    title = "1803会员购激活邮件"
    msg = " "
    # 加载激活页面
    template = loader.get_template("templates/active.html")
    html_str = template.render({'url': url})
    send_mail(
        title,
        message=msg,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[email, ],
        html_message=html_str
    )
    return token