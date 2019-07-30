# Register your models here.

from django.contrib import admin

from apptest.models import Appcase
from autotest.apitest.models import Apis
from product.models import Product
from webtest.models import Webcase


# class ProductAdmin(admin.ModelAdmin):
#     list_display = ['productname', 'productdesc', 'producter','create_time','id']

class ApisAdmin(admin.TabularInline):
    list_display = ['apiname','apiurl','apiparamvalue','apimethod','apiresult','apistatus','create_time','id','product']
    model = Apis
    extra = 1

class AppcaseAdmin(admin.TabularInline):
    list_display = ['appcasename', 'apptestresult','create_time','id','product']
    model = Appcase
    extra = 1

class WebcaseAdmin(admin.TabularInline):
    list_display = ['webcasename', 'webtestresult','create_time','id','product']
    model = Webcase
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    list_display = ['productname', 'productdesc','create_time','id']
    inlines = [ApisAdmin, AppcaseAdmin,WebcaseAdmin]

# class ProductAdmin(admin.ModelAdmin):
#     list_display = ['productname', 'productdesc','create_time','id']
#     inlines = [WebcaseAdmin]

# class ProductAdmin(admin.ModelAdmin):
#     list_display = ['productname', 'productdesc','create_time','id']
#     inlines = [AppcaseAdmin]

admin.site.register(Product) # 把产品模块注册到Django admin后台并能显示