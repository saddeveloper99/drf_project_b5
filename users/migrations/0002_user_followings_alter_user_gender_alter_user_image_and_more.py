# Generated by Django 4.2.1 on 2023-05-09 04:28

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="followings",
            field=models.ManyToManyField(
                blank=True, related_name="followers", to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="gender",
            field=models.CharField(
                choices=[("M", "Male"), ("F", "Female")],
                max_length=1,
                verbose_name="성별",
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="image",
            field=models.ImageField(
                blank=True, upload_to="profile/%Y/%m/", verbose_name="프로필 이미지"
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="introduction",
            field=models.TextField(blank=True, null=True, verbose_name="자기소개"),
        ),
        migrations.AlterField(
            model_name="user",
            name="preference",
            field=models.CharField(
                blank=True, max_length=256, null=True, verbose_name="선호 음료"
            ),
        ),
    ]
