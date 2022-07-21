from django.contrib import admin
from .models import FooterSetting, TopBarContent, SubLinks, SliderItem, CategoryBanner

# Register your models here.
class SliderItemAdmin(admin.ModelAdmin):
    list_display = ("id","title","isActive")
    list_display_links = ("id",)
    list_editable = ("isActive",)

class CategoryBannerAdmin(admin.ModelAdmin):
    list_display = ("id","title","isActive")
    list_display_links = ("id",)
    list_editable = ("isActive",)

class FooterAdmin(admin.ModelAdmin):
    list_display = ("id","edited_date")
    list_display_links = ("id",)

class SubLinkAdmin(admin.ModelAdmin):
    list_display = ("id","name","isActive")
    list_display_links = ("id","name")
    list_editable = ("isActive",)

class TopBarAdmin(admin.ModelAdmin):
    list_display = ("id","content")
    list_display_links = ("id","content")


admin.site.register(FooterSetting,FooterAdmin)
admin.site.register(SubLinks,SubLinkAdmin)
admin.site.register(TopBarContent,TopBarAdmin) 
admin.site.register(SliderItem,SliderItemAdmin) 
admin.site.register(CategoryBanner,CategoryBannerAdmin) 