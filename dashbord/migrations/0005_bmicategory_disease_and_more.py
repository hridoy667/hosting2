# Generated by Django 5.1.2 on 2024-11-15 13:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashbord', '0004_timebasedsuggestion_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='BMICategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Underweight', 'Underweight'), ('Normal', 'Normal'), ('Overweight', 'Overweight'), ('Obese', 'Obese')], max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Disease',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('General', 'General'), ('Diabetes', 'Diabetes'), ('Heart Disease', 'Heart Disease')], max_length=50, unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='timebasedsuggestion',
            name='applicable_for',
        ),
        migrations.RemoveField(
            model_name='timebasedsuggestion',
            name='suggestion_text',
        ),
        migrations.AddField(
            model_name='timebasedsuggestion',
            name='deep_work_suggestion',
            field=models.TextField(blank=True, help_text='Suggestions for focused work or activity'),
        ),
        migrations.AddField(
            model_name='timebasedsuggestion',
            name='diet_suggestion',
            field=models.TextField(blank=True, help_text='Diet suggestion for this time period'),
        ),
        migrations.AddField(
            model_name='timebasedsuggestion',
            name='nap_suggestion',
            field=models.TextField(blank=True, help_text='Nap or sleep suggestion'),
        ),
        migrations.AddField(
            model_name='timebasedsuggestion',
            name='water_intake',
            field=models.CharField(blank=True, help_text='Water intake suggestion', max_length=50),
        ),
        migrations.AddField(
            model_name='timebasedsuggestion',
            name='bmi_category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='dashbord.bmicategory'),
        ),
        migrations.AddField(
            model_name='timebasedsuggestion',
            name='disease',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='dashbord.disease'),
        ),
    ]
