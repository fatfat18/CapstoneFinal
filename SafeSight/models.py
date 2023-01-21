from django.db import models
from django.shortcuts import render, redirect



class editupdaterecord(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

    class Meta:
        db_table=""


