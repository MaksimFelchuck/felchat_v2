# Generated by Django 4.1.6 on 2023-02-12 10:06

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
            name="Post",
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
                (
                    "pub_date",
                    models.DateField(auto_now_add=True, verbose_name="Дата публикации"),
                ),
                (
                    "headline",
                    models.CharField(max_length=200, verbose_name="Заголовок"),
                ),
                ("content", models.TextField(verbose_name="Текст публикации")),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
