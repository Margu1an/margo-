from django.urls import path, include

urlpatterns = [
    path("api/", include("customers.urls")),
    path("api/", include("tables.urls")),
    path("api/", include("reservations.urls")),
]
