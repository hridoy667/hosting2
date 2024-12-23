# Generated by Django 5.1.2 on 2024-11-08 17:27

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('bmiInput', '0002_delete_userprofile'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.PositiveIntegerField()),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], default='male', max_length=6)),
                ('height_value', models.DecimalField(decimal_places=2, max_digits=5)),
                ('height_unit', models.CharField(choices=[('cm', 'cm'), ('feet', 'feet')], default='cm', max_length=5)),
                ('weight_value', models.DecimalField(decimal_places=2, max_digits=5)),
                ('weight_unit', models.CharField(choices=[('kg', 'kg'), ('pounds', 'pounds')], default='kg', max_length=7)),
                ('weekly_working_hours', models.PositiveIntegerField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
