"""marvel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from e_commerce.api.views import LoginUserAPIView 
from rest_framework import permissions
from drf_yasg import openapi
from drf_yasg.views import get_schema_view 


schema_view = get_schema_view(
    openapi.Info(
        title="Inove Marvel e-commerce",
        default_version='1.0.0',
        description="description",
        contact=openapi.Contact(email="info@inove.com.ar"),
        license=openapi.License(name="Inove Coding School."),
),
    public=True,
    permission_classes=(permissions.IsAuthenticatedOrReadOnly,),
)





urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('e-commerce/',include('e_commerce.urls')),
    path('e-commerce/api/', include('e_commerce.api.urls')),
    path('login/', LoginUserAPIView.as_view(), name="login"),
    path('api-docs/swagger',schema_view.with_ui('swagger', cache_timeout=0),name='schema-swagger-ui'),
    path('api-docs/redoc',schema_view.with_ui('redoc', cache_timeout=0),name='schema-redoc'),


]
