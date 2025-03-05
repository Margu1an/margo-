from django.urls import path
from .views import ReservationListCreate, ReservationDetail, UserReservations, UpdateReservation, DeleteReservation

urlpatterns = [
    path("reservations/", ReservationListCreate.as_view(), name="reservation-list"),
    path("reservations/<int:pk>/", ReservationDetail.as_view(), name="reservation-detail"),
    path("reservations/user/<int:user_id>/", UserReservations.as_view(), name="user-reservations"),
    path("reservations/<int:pk>/update/", UpdateReservation.as_view(), name="update-reservation"),
    path("reservations/<int:pk>/delete/", DeleteReservation.as_view(), name="delete-reservation"),
]
