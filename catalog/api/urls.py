from django import views
from django.urls import path,include

from catalog.api.views import ProductViewSet, CollectionViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"products", ProductViewSet)
router.register(r"collections", CollectionViewSet)

urlpatterns = [
    path("", include(router.urls))
]