from __future__ import unicode_literals
from django.db import models
import os
from binascii import hexlify
import datetime


def random_ref():
    return hexlify(os.urandom(16))


class ActiveObjectsManager(models.Manager):
    def get_queryset(self):
        return super(ActiveObjectsManager, self).get_queryset().filter(archived=False)


class MemberTitle(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class MemberType(models.Model):
    type = models.CharField(max_length=255)
    fee = models.FloatField(default=True)

    def __str__(self):
        return self.type


class Member(models.Model):
    type = models.ForeignKey(MemberType)
    title = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    nic = models.CharField(max_length=255, null=True, blank=True, default='N/A')
    ref_id = models.CharField(max_length=255, unique=True, default=random_ref)
    mobile = models.CharField(max_length=255, null=True, blank=True, default='N/A')
    home = models.CharField(max_length=255, null=True, blank=True, default='N/A')
    email = models.CharField(max_length=255, null=True, blank=True, default='N/A')
    remarks = models.TextField(null=True, blank=True, default='No Remark Available')
    address = models.TextField(null=True, blank=True, default='No Address Available')
    town = models.CharField(max_length=255, null=True, blank=True, default='N/A')
    image = models.TextField()
    web_active = models.BooleanField(default=False)
    username = models.CharField(max_length=255, null=True, blank=True, default='')
    password = models.TextField(default='')
    ban_status = models.BooleanField(default=False)
    registration_status = models.CharField(max_length=255, null=True, blank=True, default='Pending')
    registration_expire = models.DateTimeField(null=True, blank=True)
    archived = models.BooleanField(default=False)
    archived_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = models.Manager()  # The default manager.
    active_objects = ActiveObjectsManager()  # The Soft Delete manager.

    def __str__(self):
        return self.title + " " + self.name

    def delete(self):
        self.archived = True
        self.archived_date = datetime.datetime.now()
        self.save()
