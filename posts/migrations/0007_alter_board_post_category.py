# Generated by Django 4.2.1 on 2023-07-07 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_alter_board_post_nickname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board_post',
            name='category',
            field=models.CharField(default='', max_length=20, verbose_name='카테고리'),
        ),
    ]