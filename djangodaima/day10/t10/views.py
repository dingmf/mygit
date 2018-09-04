from django.shortcuts import render
from .models import MyWheel, MyNav, MustBuy, MyShop, MyUser, MainShow, GoodType, Goods


# Create your views here.

def home(req):
    # 拿轮播数据
    swipers = MyWheel.objects.raw("SELECT * FROM axf_wheel")
    # 拿导航数据
    navs = MyNav.objects.all()
    # 拿必购数据
    mustbys = MustBuy.objects.all()
    # 拿商店数据
    shops = MyShop.objects.all()
    shop_img = shops[0]
    # 拿商品数据
    goods = MainShow.objects.all()
    data ={
        'title': '首页',
        'swipers': swipers,
        'navs': navs,
        'must_bys': mustbys,
        'shop_img':shop_img,
        'shop_two':shops[1:3],
        'shop_more':shops[3:7],
        'shop_last': shops[7:],
        'goods': goods
    }
    return render(req, 'home/home.html', data)

def market(req, type_id, sub_type_id):
    #  拿全部的数据
    all_types = GoodType.objects.all()
    # 拿商品
    goods = Goods.objects.filter(
        categoryid=type_id
    )
    # 如果二级分类的id不等于0  那就需要在原有数据集goods的基础上  找对应二级分类对应的id
    if int(sub_type_id) != 0:
        goods = goods.filter(childcid=sub_type_id)


    # 通过查询出来的数据集找到选中的那个分类数据
    select_type = all_types.get(typeid=type_id)
    # 拿到二级分类数据
    all_sub_type = select_type.childtypenames
    # 将子类数据切分
    type_name_id_list = all_sub_type.split("#")
    # 繁琐写法，可以优化
    # sub_types = []
    # for i in type_name_id_list:
    #     name_ids = i.split(":")
    #     sub_types.append(name_ids)
    # 优化写法
    sub_types = [ i.split(':') for i in type_name_id_list]
    # print(sub_types)
    data ={
        'title': '闪购',
        'types': all_types,
        'goods':goods,
        'selected_typeid':type_id,
        'sub_types': sub_types,
        'select_sub_type_id': sub_type_id
    }
    return render(req, 'market/market.html', data)

def cart(req):
    data ={
        'title': '购物车'
    }
    return render(req, 'cart/cart.html', data)

def mine(req):
    # 那用户
    user = req.user
    # 初始化 默认值
    is_login = False
    user_name = ""
    u_icon = ""
    # 判断用户user是不是MyUser的实例
    if isinstance(user, MyUser):
        # 如果判断通过说明是登录过
        is_login = True
        user_name = user.username
        # 拼接用户头像 req.get_host() 拿到前端浏览器地址栏里输入域名加端口
        u_icon = "http://{host}/static/uploads/{icon_url}".format(
            host=req.get_host(),
            icon_url=user.icon.url
        )

    data ={
        'title': '我的',
        'is_login': is_login,
        'user_icon': u_icon,
        'user_name': user_name
    }
    return render(req, 'mine/mine.html', data)


def register_view(req):
    return render(req, 'user/register.html')

def my_login(req):
    return render(req, "user/login.html")


