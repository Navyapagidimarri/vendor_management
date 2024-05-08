from django.urls import path
from . import views

urlpatterns = [
    path('api/vendors/', views.create_vendor, name='create_vendor'),
    path('api/vendors/<int:id>/', views.update_vendor, name='update_vendor'),
    path('api/purchase_orders/', views.create_purchase_order, name='create_purchase_order'),
    path('api/purchase_orders/<int:po_id>/', views.purchase_order_detail, name='purchase_order_detail'),
     path('api/vendors/<int:vendor_id>/performance', views.get_vendor_performance, name='get_vendor_performance'),
]
