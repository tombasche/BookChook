# Generated by Django 2.0 on 2018-09-11 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0004_auto_20161013_2251'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='comment',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='location',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='number',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='status',
            field=models.CharField(choices=[('current', 'Current'), ('archived', 'Removed')], default='current', max_length=20),
        ),
    ]
