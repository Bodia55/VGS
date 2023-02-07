from django.db import models
import uuid

class Resource(models.Model):
    COMMITTEE_NAME = (
        ('GDD', 'GDD'),
        ('GSD', 'GSD'),
        ('GAD', 'GAD')
    )
    FILE_TYPE = (
        ('IMAGE', 'IMAGE'),
        ('VIDEO', 'VIDEO'),
        ('OTHER', 'OTHER')
    )
    committee = models.CharField(max_length=200, choices=COMMITTEE_NAME, null=True)
    resource_type = models.CharField(max_length=200, choices=FILE_TYPE, null=True)
    resource_name = models.CharField(max_length=200, null=False, blank=False)
    resource_data = models.FileField()
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.resource_name
