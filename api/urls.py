from django.urls import path,include
from  rest_framework.authtoken import views
from .views import *

urlpatterns = [
    path('',Home,name='api.home'),
    path('category/',include('api.category.urls')),
    path('products/',include('api.product.urls')),
    path('user/',include('api.user.urls')),
    path('order/',include('api.order.urls')),
    path('api-token-auth/',views.obtain_auth_token,name='api_token_auth'),
    path('payment/',include('api.payment.urls')),
]