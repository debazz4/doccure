# Generated by Django 5.1.5 on 2025-02-06 07:18

import localflavor.us.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doccure_app', '0005_alter_doctorprofile_specification_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctorprofile',
            name='state',
            field=localflavor.us.models.USStateField(max_length=2),
        ),
    ]
