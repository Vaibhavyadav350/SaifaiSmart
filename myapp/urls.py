# myapp/urls.py

from django.urls import path
from .views import ProductListGet,ProductListPost
urlpatterns = [
    
    path('products/get', ProductListGet.as_view(), name='get-products'),
    path('products/v1/post', ProductListPost.as_view(), name='post-products'),
]