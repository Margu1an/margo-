from rest_framework import generics
from .models import Reservation
from .serializers import ReservationSerializer
from django.http import JsonResponse
from datetime import date

class ReservationListCreate(generics.ListCreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

    def perform_create(self, serializer):
        customer = self.request.data.get("customer")
        res_date = self.request.data.get("date")
        
        existing_reservation = Reservation.objects.filter(customer=customer, date=res_date).exists()
        if existing_reservation:
            return JsonResponse({"error": "У вас уже есть бронь на этот день."}, status=400)

        serializer.save()

class ReservationDetail(generics.RetrieveAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

class UserReservations(generics.ListAPIView):
    serializer_class = ReservationSerializer

    def get_queryset(self):
        user_id = self.kwargs["user_id"]
        return Reservation.objects.filter(customer__id=user_id)

class UpdateReservation(generics.UpdateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

class DeleteReservation(generics.DestroyAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
