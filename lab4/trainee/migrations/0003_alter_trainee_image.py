# Generated by Django 5.1 on 2024-08-26 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainee', '0002_alter_trainee_account_obj_alter_trainee_track_obj'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainee',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='trainee/images/'),
        ),
    ]
