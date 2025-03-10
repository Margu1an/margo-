from django.urls import path
from .views import CustomerListCreate, CustomerDetail

urlpatterns = [
    path("customers/", CustomerListCreate.as_view(), name="customer-list"),
    path("customers/<int:pk>/", CustomerDetail.as_view(), name="customer-detail"),
]
