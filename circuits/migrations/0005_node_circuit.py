# Generated by Django 2.1.7 on 2019-02-16 16:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('circuits', '0004_circuit_uuid'),
    ]

    operations = [
        migrations.AddField(
            model_name='node',
            name='circuit',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='circuits.Circuit'),
            preserve_default=False,
        ),
    ]