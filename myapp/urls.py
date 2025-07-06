from django.urls import path
from . import views

urlpatterns = [
    path('items/<int:item_id>/', views.item_detail, name='item_detail'),
    path('show-qr/', views.show_qr, name='show_qr'),
]
