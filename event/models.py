from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    event_date = models.DateField()
    location = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='event_images/', blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    @property
    def registered_count(self):
        return self.registration_set.count()


class Registration(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    registered_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'event')

    def __str__(self):
        return f"{self.user.username} registered for {self.event.name}"
