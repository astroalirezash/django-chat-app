# Generated by Django 4.1.1 on 2022-09-27 07:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Host",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("joined", models.DateTimeField(auto_now_add=True)),
                ("name", models.CharField(max_length=100, verbose_name="نام گروه")),
                (
                    "members",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="members",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="اعضا",
                    ),
                ),
            ],
            options={"abstract": False,},
        ),
        migrations.CreateModel(
            name="Message",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("joined", models.DateTimeField(auto_now_add=True)),
                (
                    "Text",
                    models.TextField(blank=True, null=True, verbose_name="متن پیام"),
                ),
                (
                    "media",
                    models.FileField(
                        blank=True,
                        null=True,
                        upload_to="media/msg_files/",
                        verbose_name="فایل",
                    ),
                ),
                (
                    "messages",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="host",
                        to="chat.host",
                        verbose_name="گروه",
                    ),
                ),
                (
                    "owner",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="owner",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="فرستنده",
                    ),
                ),
            ],
            options={"abstract": False,},
        ),
    ]
