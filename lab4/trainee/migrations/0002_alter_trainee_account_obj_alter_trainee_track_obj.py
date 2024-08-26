# Generated by Django 5.1 on 2024-08-26 17:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
        ('track', '0001_initial'),
        ('trainee', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainee',
            name='account_obj',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='account.account'),
        ),
        migrations.AlterField(
            model_name='trainee',
            name='track_obj',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='track.track'),
        ),
    ]
