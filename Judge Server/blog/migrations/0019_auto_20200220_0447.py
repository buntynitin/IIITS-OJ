# Generated by Django 2.1.2 on 2020-02-20 04:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='post',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
