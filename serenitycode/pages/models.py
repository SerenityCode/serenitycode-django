from django.db import models
import datetime


class Project(models.Model):
    created_at = models.DateTimeField(editable=False, null=True)
    last_modified = models.DateTimeField()

    user = models.ForeignKey('auth.User')
    title = models.CharField(max_length=255)
    link = models.URLField()
    text = models.TextField()

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = datetime.datetime.now()
        self.modified = datetime.datetime.now()
        return super(Project, self).save(*args, **kwargs)