# Generated by Django 2.2.13 on 2020-06-21 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myCSBlog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='snatch',
            field=models.CharField(default='edit post to set snatch', max_length=350),
            preserve_default=False,
        ),
    ]