"""renarte URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from django.conf import settings


admin.site.site_header = "Renarte Admin Site"
admin.site.site_title = "Admin Site"
admin.site.index_title = "Welcome to Renarte Admin Site"

urlpatterns = [
    path("", include("main.urls")),
    path("catalog/", include("catalog.urls")),
    path('admin/', admin.site.urls),
    path("api/", include("catalog.api.urls")),
    path("api-auth/", include("rest_framework.urls")), # Browsable api sayfasında login-logout işlemleri yapabilmek için
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
