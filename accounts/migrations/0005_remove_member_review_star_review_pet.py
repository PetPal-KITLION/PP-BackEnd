# Generated by Django 4.2.1 on 2023-07-07 05:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0004_member_address_member_age_member_review_star"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="member",
            name="review_star",
        ),
        migrations.CreateModel(
            name="Review",
            fields=[
                (
                    "id",
                    models.AutoField(primary_key=True, serialize=False, unique=True),
                ),
                ("content", models.TextField(default="", verbose_name="리뷰내용")),
                ("score", models.IntegerField(verbose_name="점수")),
                (
                    "member",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="reviews",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Pet",
            fields=[
                (
                    "id",
                    models.AutoField(primary_key=True, serialize=False, unique=True),
                ),
                ("name", models.CharField(max_length=100, verbose_name="펫이름")),
                ("species", models.CharField(max_length=100, verbose_name="종")),
                ("age", models.IntegerField(verbose_name="펫나이")),
                ("feature", models.TextField(verbose_name="펫특이사항")),
                (
                    "member",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="pets",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
