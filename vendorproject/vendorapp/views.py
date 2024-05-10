from django.http import JsonResponse
from .models import vendor_profile,PurchaseOrder
from .serializers import vendorSerializer,PurchaseOrderSerializer
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework import status 

@api_view(['POST','GET'])
def create_vendor(request): 
       if request.method == 'GET':
        vendors = vendor_profile.objects.all()
        serializer = vendorSerializer(vendors, many=True)
        return JsonResponse(serializer.data, safe=False)

       if request.method == 'POST':
        serializer = vendorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
@api_view(['GET', 'PUT', 'DELETE'])
def update_vendor(request, id):
    try:
        ven = vendor_profile.objects.get(pk=id)
    except ven.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = vendorSerializer(ven)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = vendorSerializer(ven, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        ven.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST', 'GET'])
def create_purchase_order(request):
    if request.method == 'POST':
        serializer = PurchaseOrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'GET':
        vendor_id = request.query_params.get('vendor_id')
        if vendor_id:
            purchase_orders = PurchaseOrder.objects.filter(vendor_reference=vendor_id)
        else:
            purchase_orders = PurchaseOrder.objects.all()
        serializer = PurchaseOrderSerializer(purchase_orders, many=True)
        return Response(serializer.data)

@api_view(['GET', 'PUT', 'DELETE'])
def purchase_order_detail(request, po_id):
    try:
        purchase_order = PurchaseOrder.objects.get(pk=po_id)
    except PurchaseOrder.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PurchaseOrderSerializer(purchase_order)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PurchaseOrderSerializer(purchase_order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        purchase_order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET','POST'])
def get_vendor_performance(request, vendor_id):
    if request.method=="GET":
     serializer = vendorSerializer(vendor)
     return Response(serializer.data) 
    elif request.method == 'POST':
        vendor.on_time_delivery_rate = request.data.get('on_time_delivery_rate', vendor.on_time_delivery_rate)
        vendor.quality_rating = request.data.get('quality_rating', vendor.quality_rating)
        vendor.response_time = request.data.get('response_time', vendor.response_time)
        vendor.fulfillment_rate = request.data.get('fulfillment_rate', vendor.fulfillment_rate)
        vendor.save()
        return Response({'message': 'Vendor performance updated successfully'}, status=status.HTTP_201_CREATED)
