from django.shortcuts import get_object_or_404
from .models import FooterSetting, SubLinks, TopBarContent, SliderItem, CategoryBanner


sub_links = SubLinks.objects.all()
slider_items = SliderItem.objects.filter(isActive=True)
category_banners = CategoryBanner.objects.filter(isActive=True)
top_bar = get_object_or_404(TopBarContent, pk=1)
settings =  get_object_or_404(FooterSetting, pk = 1)

context = {
    "settings": settings,       #footer settings
    "sub_links" : sub_links,    #header sublinks
    "top_bar": top_bar,
    "slider_items" : slider_items,
    "category_banners" : category_banners,
    
}