from django.db import models

from account.models import User

# Create your models here.

class BaseModel(models.Model):
   joined = models.DateTimeField(auto_now_add=True)

   class Meta:
       abstract = True


class Message(BaseModel):
    owner = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='فرستنده', related_name='owner')
    Text = models.TextField(verbose_name='متن پیام', null=True, blank=True)
    media = models.FileField(verbose_name='فایل', null=True, blank=True)


class Host(BaseModel):
    messages = models.ForeignKey(Message, on_delete=models.CASCADE, verbose_name='پیام ها', related_name='messages')
    members = models.ManyToManyField(User, verbose_name='اعضا', related_name='members')
    
