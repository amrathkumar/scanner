from django.urls import path
from . import views

urlpatterns = [
    path('items/<int:item_id>/', views.item_detail, name='item_detail'),
    path('', views.show_qr, name='show_qr'),
    path("search-product", views.search_product, name="search_product"),
    path("add-product", views.add_product, name="add_product"),
]
