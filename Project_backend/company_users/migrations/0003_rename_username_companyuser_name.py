# Generated by Django 5.1 on 2024-08-29 10:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company_users', '0002_rename_user_type_companyuser_type_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='companyuser',
            old_name='username',
            new_name='name',
        ),
    ]
