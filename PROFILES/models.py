from django.db import models
import uuid

class Profile(models.Model):
    member_id = models.CharField(max_length=200, null=True, blank=True)
    is_admin = models.BooleanField(default=False)
    password = models.CharField(max_length=2000)
    sessionId = models.UUIDField(default=uuid.uuid4, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.member_id