from rest_framework import routers
from django.urls import path,include
from . import views

router = routers.DefaultRouter()
router.register(r'',views.CatogeryViewsets )

urlpatterns = [
    path('',include(router.urls))

]