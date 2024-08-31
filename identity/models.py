from django.db import models

ROLE_CHOICES = [
    ('admin', 'Admin'),
    ('rider', 'Rider'),
    ('driver', 'Driver'),
]

class User(models.Model):
    id_user = models.AutoField(primary_key=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='rider')
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.email

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}".strip()

    def get_short_name(self):
        return self.first_name
