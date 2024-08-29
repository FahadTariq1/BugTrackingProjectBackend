# Generated by Django 5.1 on 2024-08-29 08:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bugs', '0001_initial'),
        ('company_users', '0002_rename_user_type_companyuser_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bug',
            name='assigneduser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_detials', to='company_users.companyuser'),
        ),
    ]
