# Generated by Django 3.0.6 on 2020-07-09 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20200709_1607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='url',
            field=models.URLField(blank=True, default='nothing', null=True),
        ),
    ]
