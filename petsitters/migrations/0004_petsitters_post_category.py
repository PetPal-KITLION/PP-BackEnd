# Generated by Django 4.2.2 on 2023-07-05 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petsitters', '0003_rename_member_id_petsitters_post_member'),
    ]

    operations = [
        migrations.AddField(
            model_name='petsitters_post',
            name='category',
            field=models.CharField(choices=[('1', '일반'), ('2', '프리미엄')], default='1', max_length=1, verbose_name='카테고리'),
        ),
    ]
