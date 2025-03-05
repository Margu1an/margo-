from django.db import models

class Reservation(models.Model):
    STATUS_CHOICES = [
        ("pending", "Ожидает"),
        ("confirmed", "Подтверждено"),
        ("cancelled", "Отменено"),
    ]

    customer = models.ForeignKey("customers.Customer", on_delete=models.CASCADE)
    table = models.ForeignKey("tables.Table", on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="pending")

    def __str__(self):
        return f"Reservation {self.id} - {self.status}"
