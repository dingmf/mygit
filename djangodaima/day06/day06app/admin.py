from django.contrib import admin
from .models import Player, Humen

# Register your models here.

class HumenInfo(admin.TabularInline):
#     指定model
    model = Humen
# 指定增加的条数
    extra = 2


class PlayerAdmin(admin.ModelAdmin):
    def get_rate_level(self):
        if self.rate >=9:
            return "好书"
        else:
            return "求求你撕了吧"
    get_rate_level.short_description = "评价"


    list_display = ['name', 'rate', get_rate_level]
    list_filter = ['rate', 'desc']
    search_fields = ['name', 'rate']
    list_per_page = 1
    fieldsets = [
        ("基本信息", {'fields': ("name", "desc", )}),
        ("附加信息", {'fields': ("rate", "extra")})
    ]
    inlines = [HumenInfo]

# 注册你的model
admin.site.register(Player, PlayerAdmin)
admin.site.register(Humen)
