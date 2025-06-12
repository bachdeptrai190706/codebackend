from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('cart/', views.cart_view, name='cart_view'),
    path('cart/increase/<int:item_id>/', views.increase_quantity, name='increase_quantity'),
    path('cart/decrease/<int:item_id>/', views.decrease_quantity, name='decrease_quantity'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),  # 👈 thêm dòng này
    path('checkout/', views.checkout_view, name='checkout'),
]
