from __future__ import unicode_literals
from django.db import models
import datetime


# Create your models here.


class ActiveObjectsManager(models.Manager):
    def get_queryset(self):
        return super(ActiveObjectsManager, self).get_queryset().filter(archived=False)


class BookCategory(models.Model):
    cat_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.cat_name


class BookDetail(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    editor = models.CharField(max_length=255, null=True, blank=True, default='N/A')
    publisher = models.CharField(max_length=255, null=True, blank=True, default='N/A')
    published_year = models.CharField(max_length=255, null=True, blank=True, default='N/A')
    category = models.ForeignKey(BookCategory)
    isbn = models.CharField(max_length=255, null=True, blank=True, default='N/A')
    cl_num = models.CharField(max_length=255, null=True, blank=True, default='N/A')
    series = models.CharField(max_length=255, null=True, blank=True, default='N/A')
    series_num = models.CharField(max_length=255, null=True, blank=True, default='N/A')
    pages = models.CharField(max_length=255, null=True, blank=True, default='N/A')
    height = models.CharField(max_length=255, null=True, blank=True, default='N/A')
    image = models.TextField()
    remarks = models.TextField(null=True, blank=True, default='No Remark Available')
    summary = models.TextField(null=True, blank=True, default='No Summary Available')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_copies(self):
        copies = BookCopy.objects.filter(book_detail=self, archived=False)
        return copies

    def count_copies(self):
        total = self.get_copies().count()
        return total

    def count_available_copies(self):
        available = self.get_copies().filter(taken=False).count()
        return available

    def count_reserved_copies(self):

        # TODO:// implement this once the reservation model is completed
        reserved = 0
        return reserved

    def count_taken_copies(self):
        taken = self.get_copies().filter(taken=True).count()
        return taken


class BookCopy(models.Model):

    book_detail = models.ForeignKey(BookDetail, on_delete=models.CASCADE)
    taken = models.BooleanField(default=False)
    return_date = models.DateField(null=True,  blank=True)
    archived_date = models.DateField(null=True,  blank=True)
    archived = models.BooleanField(default=False)
    ref_id = models.CharField(max_length=255, unique=True)
    remarks = models.TextField(null=True, blank=True, default='No Remark Available')

    objects = models.Manager()  # The default manager.
    active_objects = ActiveObjectsManager()  # The Soft Delete manager.

    def __str__(self):
        return self.ref_id + " - " + self.book_detail.title

    def delete(self):
        self.archived = True
        self.archived_date = datetime.datetime.now()
        self.save()
