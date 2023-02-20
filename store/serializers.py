from rest_framework import serializers
from .models import Product,Review,Contact,rating,Order
class productserial(serializers.Serializer):
    class Meta:
        model=Product
        fields='__all__'
class Reviewserial(serializers.Serializer):
    class Meta:
        model=Review
        fields='__all__'
class contactserail(serializers.Serializer):
    class Meta:
        model=Contact
        fields='__all__'
class orderserial(serializers.Serializer):
    class Meta:
        model=Order
        fields='__all__'
