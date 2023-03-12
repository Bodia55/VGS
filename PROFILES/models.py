from django.db import models
import uuid

class Profile(models.Model):
    guc_id = models.CharField(max_length=200)
    password = models.CharField(max_length=2000)
    xp = models.PositiveBigIntegerField(default=0, null=True, blank=True)
    sessionId = models.UUIDField(default=uuid.uuid4, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.guc_id