# Generated by Django 3.0.6 on 2020-07-09 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20200709_1212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='date_writing',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
