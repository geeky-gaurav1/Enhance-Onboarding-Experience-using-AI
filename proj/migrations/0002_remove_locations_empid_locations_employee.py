# Generated by Django 5.0.4 on 2024-04-26 19:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proj', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='locations',
            name='empid',
        ),
        migrations.AddField(
            model_name='locations',
            name='employee',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Location', to='proj.employee'),
        ),
    ]
