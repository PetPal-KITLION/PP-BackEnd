# Generated by Django 4.2.2 on 2023-07-05 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_remove_board_post_comment_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='board_post',
            name='category',
            field=models.CharField(choices=[('1', '소통'), ('2', '정보')], default='1', max_length=1, verbose_name='카테고리'),
        ),
    ]