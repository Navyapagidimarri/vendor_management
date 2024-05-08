from django.db import models

# Create your models here.
class vendor_profile(models.Model):
    name=models.CharField(max_length=100)
    contact_details=models.TextField(max_length=11)
    address=models.TextField(max_length=100)
    vendor_code=models.CharField(max_length=5)
    on_time_delivery_rate=models.FloatField()
    quality_rating_avg=models.FloatField()
    average_response_time=models.FloatField()
    fulfillment_rate=models.FloatField()
class PurchaseOrder(models.Model):
    PO_number = models.CharField(max_length=50)
    vendor_reference = models.CharField(max_length=100)
    order_date = models.DateField()
    items = models.TextField()  # Assuming items will be stored as a text field
    quantity = models.IntegerField()
    status = models.CharField(max_length=20)

    def __str__(self):
        return self.PO_number
