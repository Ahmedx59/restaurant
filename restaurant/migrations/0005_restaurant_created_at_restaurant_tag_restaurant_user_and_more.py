# Generated by Django 5.1.2 on 2024-11-25 18:40

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0004_table_max_people_alter_table_available_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='created_at',
            field=models.DateTimeField(default='2024-11-25 18:34:26.152552+00:00', verbose_name=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='restaurant',
            name='tag',
            field=models.CharField(choices=[('n', 'New'), ('l', 'Luxury'), ('d', 'Discount')], default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='restaurant',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='restaurants', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='table',
            name='available',
            field=models.BooleanField(default=True, verbose_name=''),
        ),
    ]
