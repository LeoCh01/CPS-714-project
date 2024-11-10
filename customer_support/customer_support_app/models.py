from django.db import models

class Ticket(models.Model):
    id = models.AutoField(primary_key=True)
    status = models.CharField(max_length=255)
    priority = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    user = models.ForeignKey('User', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
        