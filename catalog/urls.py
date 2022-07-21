from django import views
from django.urls import path
from . import views


urlpatterns = [
    path("", views.catalog, name="catalog"),
    path("product/<slug:slug>", views.product_details, name="product_details"), 
    # path("category/<slug:slug>", views.products_by_category, name="products_by_category"), 
]
