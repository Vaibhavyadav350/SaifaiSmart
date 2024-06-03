from django.urls import path
from .views import ProductListGet,ProductListPost
from myapp import views
urlpatterns = [
    path('', views.default_view, name='default_view'),
    path('products/get', ProductListGet.as_view(), name='get-products'),
    path('products/v1/post', ProductListPost.as_view(), name='post-products'),

]