from django.contrib import admin
from .models import CareInstruction, DesignDirection, Product, ProductVariantImages, Usage, Composition, Collection, CollectionImages, Feature
from django.utils.safestring import mark_safe

class CollectionImagesInline(admin.StackedInline):
    model = CollectionImages

class ProductVariantImagesInline(admin.StackedInline):
    model = ProductVariantImages

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "collection",
        "selected_usages",
        "selected_compositions",
        "selected_features",
        "width",
        "is_active",
        "is_new",
        "is_exclusive",
        "is_contract",)

    list_editable = (
        "is_active",
        "is_new",
        "is_exclusive",
        "is_contract",
        "width")

    search_fields = ("name",
    "usages",
    "compositions")
    
    readonly_fields = ("slug",)

    list_filter = (
        "name",
        "usages",
        "compositions",
        "is_active",
        "is_new",
        "is_exclusive",
        "is_contract")

    inlines = [ProductVariantImagesInline]

    def selected_usages(self, obj):
        html = "<ul>"

        for usage in obj.usages.all():
            html += "<li>" + usage.name + "</li>"

        html += "</ul>"
        return mark_safe(html)
    
    def selected_compositions(self, obj):
        html = "<ul>"

        for composition in obj.compositions.all():
            html += "<li>" + composition.name + "</li>"

        html += "</ul>"
        return mark_safe(html)
    
    def selected_features(self, obj):
        html = "<ul>"

        for feature in obj.features.all():
            html += "<li>" + feature.name + "</li>"

        html += "</ul>"
        return mark_safe(html)


class CollectionAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "selected_products",
        "subtitle",
        "is_active",
        "is_new",
        "is_exclusive",
        "is_contract")

    list_editable = (
        "is_active",
        "is_new",
        "is_exclusive",
        "is_contract")
    
    list_filter = (
        "title",
        "is_active",
        "is_new",
        "is_exclusive",
        "is_contract")
    
    readonly_fields = ("slug",)

    inlines = [CollectionImagesInline]

    def selected_products(self, obj):
        html = "<ul>"
        
        products = Product.objects.filter(collection__title=obj.title) 
        
        for product in products:
            html += "<li>" + product.name + "</li>"

        html += "</ul>"
        return mark_safe(html)

admin.site.register(Product,ProductAdmin)
admin.site.register(Collection,CollectionAdmin)
admin.site.register(Usage)
admin.site.register(Composition)
admin.site.register(Feature)
admin.site.register(CareInstruction)
admin.site.register(DesignDirection)


