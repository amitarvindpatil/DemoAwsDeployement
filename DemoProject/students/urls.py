
from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [

    path('students/', views.get_post_product.as_view(),
         name="get_post_product"),
]         