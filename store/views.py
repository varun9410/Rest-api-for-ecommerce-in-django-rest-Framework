from django.shortcuts import render
from rest_framework.views import APIView
from .models import Product,Review,Contact,rating,Order
from rest_framework.response import Response
from .serializers import productserial,Reviewserial,orderserial
# Create your views here.
class productlist(APIView):
    def get(self,request):
        object=Product.objects.all()
        serial=productserial(object)
        return Response(serial.data)
    
class productdetail(APIView):
    def post(self,request,id):
        object=Product.objects.filter(id=id)
        serial=productserial(object)
        return Response(serial.data)
class reviewlist(APIView):
    def post(self,request,id):
        object=Review.objects.filter(Product_id=id)
        serial=Reviewserial(object)
        return Response(serial.data)
class MyOrderView(APIView):
    def get(self,request):
        object=Order.objects.all()
        serial=orderserial(object)
        return Response(serial.data)
    def post(self, request):
        serializer = orderserial(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data['name']
            email = serializer.validated_data['email']
            address = serializer.validated_data['address']
            phone_number=serializer.validated_data['phone_number']
            date=serializer.validated_date['date']
            return Response({'status': 'success'})
        else:
            return Response(serializer.errors, status=400)
