from rest_framework import serializers
from .models import vendor_profile ,PurchaseOrder

class vendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = vendor_profile
        fields = "__all__"
class PurchaseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=PurchaseOrder
        fields = "__all__"
