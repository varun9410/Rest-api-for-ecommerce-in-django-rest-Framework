from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('products',productlist.as_view(),name='productlist'),
    path('detail/<int:id>',productdetail.as_view(),name='productdetail'),
    path('review/<int:id>',reviewlist.as_view(),name='reviewlist')
]