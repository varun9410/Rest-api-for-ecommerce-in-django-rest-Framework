from django.contrib import admin

# Register your models here.
from .models import Product,Contact,Category,Review,rating,Order
admin.site.register(Product)
admin.site.register(Contact)
admin.site.register(Category)
admin.site.register(Review)
admin.site.register(rating)
admin.site.register(Order)


