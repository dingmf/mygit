# def register(req):
#     if req.method =="GET":
#         return render(req,"my_register.html")
#     else:
#         params = req.POST
#         u_name = params.get("u_name")
#         u_email = params.get("u_email")
#         u_phone = params.get("u_phone")
#         pwd = params.get("pwd")
#         confirm_pwd = params.get("confirm_pwd")
#         icon = req.FILES['u_icon']
#         # random_str = get_random_str()
#         #判断用户的输入是否满足基本要求
#         if u_name and len(u_name)>6 and pwd and confirm_pwd and pwd == confirm_pwd:
#             # 判断用户是否已经被注册
#             exists_flag = MyUser.objects.filter(username=u_name).exists()
#             if exists_flag :
#                 return HttpResponse("该用户被注册")
#             else:
#                 #如果没有被注册，那么就创建用户
#                 user = MyUser.objects.create_user(username=u_name,email=u_email,password=pwd,phone=u_phone)
#                 # 生成随机字符
#                 random_str = get_str()
#                 # 拼接验证连接
#                 url = "http://10.3.133.35:8000/homework/active/" + random_str
#                 # 加载激活模板
#                 tmp = loader.get_template('active.html')
#                 # 渲染
#                 html_str = tmp.render({'url': url})
#                 print(html_str)
#
#                 # 准备邮箱数据
#                 title = "邮箱验证"
#                 msg = ""
#                 email_from = settings.DEFAULT_FROM_EMAIL
#                 reciever = [
#                     u_email,
#                 ]
#                 send_mail(title, msg, email_from, reciever, html_message=html_str)
#                 cache.set(random_str, u_email, 120)
#                 user.icon = icon
#                 user.save()
#                 return render(req,'my_login.html')
#         else:
#             return HttpResponse("账号密码格式错误")

for i in range(4):
    print("??")