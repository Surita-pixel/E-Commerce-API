from django.urls import include, re_path
from django.urls import path

from . import views

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'items', views.ItemApiView)
urlpatterns = [
    #path('', views.index,name='index'),
    re_path(r'', include(router.urls))
]