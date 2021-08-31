"""movies_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from rest_framework import routers
from movies.view_sets import MoviesViewSet
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Movies API",
      default_version='v1',
      description="Movies database from imdb. Use /movies/ end point to access the data",
      contact=openapi.Contact(email="yago.alves105@gmail.com"),
   ),
   public=True,
)

router = routers.SimpleRouter()
router.register(r'movies', MoviesViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('documentation/', schema_view.with_ui('swagger', cache_timeout=0), 
         name='schema-swagger-ui'),
]

urlpatterns += router.urls
