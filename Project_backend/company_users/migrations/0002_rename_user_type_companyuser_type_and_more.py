# Generated by Django 5.1 on 2024-08-26 09:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company_users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='companyuser',
            old_name='user_type',
            new_name='type',
        ),
        migrations.RenameField(
            model_name='companyuser',
            old_name='user_name',
            new_name='username',
        ),
    ]
