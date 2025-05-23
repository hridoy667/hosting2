# Generated by Django 5.1.2 on 2024-11-15 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashbord', '0006_alter_timebasedsuggestion_bmi_category_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TimeBasedActivity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_period', models.CharField(choices=[('Morning', '9 AM - 12 PM'), ('Afternoon', '1 PM - 3 PM'), ('Evening', '3 PM - 5 PM')], max_length=20, unique=True)),
                ('activity_type', models.CharField(choices=[('Deep Work', 'Deep Work'), ('Nap', 'Nap')], max_length=20)),
                ('suggestion_text', models.TextField()),
            ],
        ),
    ]
