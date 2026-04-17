from django.db import models

class Account(models.Model):
    issuer = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    secret = models.CharField(max_length=255)  # no encryption for now
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.issuer} ({self.name})"