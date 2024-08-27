# Generated by Django 5.1 on 2024-08-26 14:03

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('company_users', '0002_rename_user_type_companyuser_type_and_more'),
        ('projects', '0003_rename_assigneduser_project_manager'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bug',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('screenshot_type', models.CharField(blank=True, choices=[('png', 'PNG'), ('gif', 'GIF')], max_length=3, null=True)),
                ('bug_type', models.CharField(choices=[('pending', 'Pending'), ('inprogress', 'In Progress'), ('closed', 'Closed')], default='pending', max_length=20)),
                ('due_date', models.DateField(blank=True, default=django.utils.timezone.now)),
                ('assignedproject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_details', to='projects.project')),
                ('assigneduser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bug_user', to='company_users.companyuser')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
