# Generated by Django 3.1.6 on 2021-06-24 20:22

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0003_delete_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=30, unique=True)),
                ('password', models.CharField(default='', editable=False, max_length=100)),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('user_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('is_staff', models.BooleanField(default=False, help_text='Determines if user can access the admin site', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True)),
                ('is_superuser', models.BooleanField(default=False)),
                ('list_courses', models.ManyToManyField(blank=True, to='myapi.Course')),
            ],
            options={
                'db_table': 'login',
            },
        ),
    ]
