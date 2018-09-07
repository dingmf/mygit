from django.contrib import admin
from .models import Player, Humen

# Register your models here.

class HumenInfo(admin.TabularInline):
    # 指定model
    model = Humen
    # 指定增加的条数
    extra = 2

class PlayerAdmin(admin.ModelAdmin):

    def get_rate_level(self):
        if self.rate > 9:
            return "玩"
        else:
            return "不玩"
    get_rate_level.short_description = "评价"

    # 显示
    list_display = ['name', 'rate', 'desc', get_rate_level]
    # 过滤器
    list_filter = ['rate', 'desc']
    # 搜索
    search_fields = ['name']
    # 分页
    list_per_page = 1
    # 信息分组
    fieldsets = [
        ("基本信息", {"fields": ("name", "desc")}),
        ("附加信息", {"fields": ("rate", "extra")})
    ]
    inlines = [HumenInfo]

# 注册你的model
admin.site.register(Player, PlayerAdmin)
admin.site.register(Humen)

# class MyAdmin(admin.AdminSite):
#     # 管理网页的页头部的标题
#     site_header = "qwer"
#     # 浏览窗口显示的页面名称
#     site_title = "asdf"
#     # 查看站点的跳转，
#     site_url = "http://www.baidu.com"
#
# site = MyAdmin()
# site.register(Player, PlayerAdmin)


