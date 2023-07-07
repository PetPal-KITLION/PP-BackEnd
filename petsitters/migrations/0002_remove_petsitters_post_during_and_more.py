# Generated by Django 4.2.2 on 2023-07-06 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petsitters', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='petsitters_post',
            name='during',
        ),
        migrations.AddField(
            model_name='petsitters_post',
            name='data_end',
            field=models.CharField(max_length=100, null=True, verbose_name='임시보호 종료 날짜'),
        ),
        migrations.AddField(
            model_name='petsitters_post',
            name='data_start',
            field=models.CharField(max_length=100, null=True, verbose_name='임시보호 시작 날짜'),
        ),
        migrations.AddField(
            model_name='petsitters_post',
            name='etc',
            field=models.CharField(max_length=200, null=True, verbose_name='기타사항'),
        ),
        migrations.AddField(
            model_name='petsitters_post',
            name='phone_number',
            field=models.CharField(max_length=15, null=True, verbose_name='연락처'),
        ),
        migrations.AlterField(
            model_name='petsitters_post',
            name='address',
            field=models.CharField(default='', max_length=200, verbose_name='주소'),
        ),
        migrations.AlterField(
            model_name='petsitters_post',
            name='category',
            field=models.CharField(choices=[('1', '시터신청'), ('2', '시터찾기')], default='1', max_length=1, verbose_name='시터등급'),
        ),
        migrations.AlterField(
            model_name='petsitters_post',
            name='pay',
            field=models.IntegerField(default=0, verbose_name='임시보호 수수료'),
        ),
    ]