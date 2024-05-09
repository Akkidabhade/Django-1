from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('products/', views.products, name='products'),
    path('contact/', views.contact, name='contact'),
    path('search/',views.search,name='search'),
    path('login/',views.user_login,name='login'),
    path('signup/',views.user_signup,name='signup'),
    path('logout/',views.user_logout,name='logout'),
    path('', views.product_list, name='product_list'),
    path('cart/',views.view_cart, name='view_cart'),
    path('add/<int:product_id>', views.add_to_cart, name='add_to_cart'),
    path('remove/<int:item_id>', views.remove_from_cart, name='remove_from_cart'),

]
