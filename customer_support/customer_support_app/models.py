from django.db import models

class Ticket(models.Model):
    ticket_id = models.AutoField(primary_key=True)
    status = models.CharField(max_length=255)
    priority = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    user_id = models.ForeignKey('User', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    ticket_response = models.ForeignKey('TicketResponse', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class ChatLogs(models.Model):
    chat_id = models.AutoField(primary_key=True)
    message = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    user_id = models.ForeignKey('User', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class TicketResponse(models.Model):
    Ticket_Response_ID = models.AutoField(primary_key=True)
    User_ID = models.CharField(max_length=255)
    Response_text = models.CharField(max_length=255)
    Responded_at = models.CharField(max_length=255)
    Tickets_Ticket_ID = models.ForeignKey('User', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
 