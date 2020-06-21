from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings
from django.utils import timezone


# Create your models here.
class Post(models.Model):

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # set forign key constraint. Cascade delete child table rows.
    title = models.CharField(max_length=200)                                        # VARCHAR(200)
    text = models.TextField()                                                       # Text field
    snatch = models.CharField(max_length=500)
    created_date = models.DateTimeField(default=timezone.now)                       # DateTime field set to now on creation
    published_date = models.DateTimeField(blank=True, null=True)                    # Blank Nullable field

    # When published update record with publish data
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    # To String returns model title
    def __str__(self):
        return self.title
