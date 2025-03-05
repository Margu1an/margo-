from django.urls import path
from .views import TableListCreate, AvailableTables

urlpatterns = [
    path("tables/", TableListCreate.as_view(), name="table-list"),
    path("tables/available/", AvailableTables.as_view(), name="table-available"),
]
