# Generated by Django 3.1 on 2020-09-10 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0012_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title_tag',
            field=models.CharField(max_length=255, verbose_name='Title Tag'),
        ),
    ]
