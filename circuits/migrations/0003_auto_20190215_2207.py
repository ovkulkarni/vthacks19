# Generated by Django 2.1.7 on 2019-02-16 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('circuits', '0002_circuit_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='circuit',
            name='original_image',
            field=models.ImageField(default='/Users/okulkarni/TJHSST/CS/vthacks19/imgs/1.JPG', upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='circuit',
            name='processed_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
