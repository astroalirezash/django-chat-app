from django.db import models

from account.models import User

# Create your models here.

class BaseModel(models.Model):
   joined = models.DateTimeField(auto_now_add=True)

   class Meta:
       abstract = True


class Host(BaseModel):
    name = models.CharField(verbose_name='نام گروه', max_length=100)
    members = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='اعضا', related_name='members')


class Message(BaseModel):
    owner = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='فرستنده', related_name='owner')
    messages = models.ForeignKey(Host, on_delete=models.CASCADE, verbose_name='گروه', related_name='host')
    Text = models.TextField(verbose_name='متن پیام', null=True, blank=True)
    media = models.FileField(verbose_name='فایل', null=True, blank=True, upload_to='media/msg_files/')
