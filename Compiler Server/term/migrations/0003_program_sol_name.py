# Generated by Django 3.0.3 on 2020-03-12 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('term', '0002_auto_20200311_1202'),
    ]

    operations = [
        migrations.AddField(
            model_name='program',
            name='sol_name',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
