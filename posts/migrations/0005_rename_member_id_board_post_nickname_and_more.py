# Generated by Django 4.2.1 on 2023-07-07 13:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_alter_board_post_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='board_post',
            old_name='member_id',
            new_name='nickname',
        ),
        migrations.RemoveField(
            model_name='board_comment',
            name='likes',
        ),
        migrations.RemoveField(
            model_name='board_post',
            name='likes',
        ),
        migrations.AddField(
            model_name='board_post',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='posts/uploads/', verbose_name='첨부파일'),
        ),
        migrations.AlterField(
            model_name='board_comment',
            name='post_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.board_post'),
        ),
        migrations.AlterField(
            model_name='board_post',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]