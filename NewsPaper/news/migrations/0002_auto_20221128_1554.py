# Generated by Django 3.2.16 on 2022-11-28 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='comment_rating',
        ),
        migrations.AddField(
            model_name='comment',
            name='grade',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='author',
            name='rating',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='grade',
            field=models.SmallIntegerField(default=0),
        ),
    ]
