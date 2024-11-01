# Generated by Django 5.1.2 on 2024-11-01 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('description', models.CharField(max_length=255)),
                ('created_at', models.DateField()),
                ('delivery_date', models.DateField()),
            ],
        ),
    ]