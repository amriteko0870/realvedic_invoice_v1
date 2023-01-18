from django.db import models


class UserCreds(models.Model):
    name = models.TextField(blank=False,null=True)
    email = models.TextField(blank=False,null=False)
    password = models.TextField(blank=False,null=False)
    token = models.TextField(blank=False,null=False)
    user_type = models.CharField(max_length=1,default='u',choices=(('u','u'),('s','s')))