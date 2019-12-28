from django.db import models
from django.contrib.auth.models import AbstractUser


class Invoices(models.Model):
    date = models.DateField()
    number = models.CharField(max_length=18, verbose_name='Number')
    supply = models.DateField(verbose_name='Supply')
    comment = models.TextField(max_length=36, default="No comment", verbose_name='Comment')

    class Meta(AbstractUser.Meta):
        pass


    def __str__(self):
        return "Invoices"




class My_user(AbstractUser):
    is_admin = models.BooleanField('admin status', default=False)
    is_moderator = models.BooleanField('moderator status', default=False)

    class Meta(AbstractUser.Meta):
        pass


    def __str__(self):
        return "User"


