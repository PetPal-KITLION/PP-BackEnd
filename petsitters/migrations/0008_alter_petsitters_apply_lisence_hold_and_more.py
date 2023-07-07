# Generated by Django 4.2.1 on 2023-07-07 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petsitters', '0007_alter_petsitters_post_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='petsitters_apply',
            name='lisence_hold',
            field=models.CharField(default='', max_length=20, verbose_name='자격증 보유여부'),
        ),
        migrations.AlterField(
            model_name='petsitters_apply',
            name='pet_experience',
            field=models.CharField(default='', max_length=20, verbose_name='반려동물 경험'),
        ),
        migrations.AlterField(
            model_name='petsitters_apply',
            name='pet_species',
            field=models.CharField(default='', max_length=20, verbose_name='동물 종류'),
        ),
    ]
