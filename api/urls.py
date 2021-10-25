from django.urls import path
from api.views import *

urlpatterns = [
    path('produto/<int:codigo>', get_produto, name='get_product_info'),
]