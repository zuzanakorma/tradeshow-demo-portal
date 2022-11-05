from django.conf import settings
from django.db import models
from django.db.models import Q
from django_resized import ResizedImageField


class Tag(models.Model):
    caption = models.CharField(max_length=20)

    def __str__(self):
        return self.caption


class CardQuerySet(models.QuerySet):
    def search(self, query=None):
        qs = self
        if query is not None:
            or_lookup = (Q(title__icontains=query) |
                         Q(description__icontains=query)
                         )
            qs = qs.filter(or_lookup, visible=True).distinct()
        return qs


class CardManager(models.Manager):
    def get_queryset(self):
        return CardQuerySet(self.model, using=self._db)

    def search(self, query=None):
        return self.get_queryset().search(query=query)


class Card(models.Model):
    title = models.CharField(max_length=32)
    image = ResizedImageField(size=[200, 200], scale=None, crop=[
                              'middle', 'center'], upload_to="images", null=True)
    description = models.CharField(max_length=32)
    url = models.URLField()
    username = models.CharField(max_length=128)
    password = models.CharField(max_length=128)
    visible = models.BooleanField(default=True)
    tags = models.ManyToManyField(Tag)

    my_order = models.PositiveSmallIntegerField(
        default=0, blank=False, null=False)

    def __str__(self):
        return str(self.title)

    def delete(self, using=None, keep_parents=False):
        self.image.delete()
        super().delete()

    class Meta:
        ordering = ['my_order']

    objects = CardManager()
