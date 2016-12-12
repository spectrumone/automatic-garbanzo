from __future__ import unicode_literals

from django.db import models

from taggit.managers import TaggableManager
from core.models import TimeStampedModel


class Project(TimeStampedModel):
    title = models.CharField(max_length=128, blank=True)
    frontpage_photo = models.ImageField()
    summary = models.TextField(blank=True)
    text = models.TextField(blank=True)
    tags = TaggableManager()

    def __unicode__(self):
        return self.title


class Photo(TimeStampedModel):
    project = models.ForeignKey(Project, related_name="photos")
    photo = models.ImageField()

    def __unicode__(self):
        return self.project.title + ' photo ' + str(self.pk)
