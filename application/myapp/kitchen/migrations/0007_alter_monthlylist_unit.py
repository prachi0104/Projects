# Generated by Django 5.0.4 on 2024-04-23 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kitchen', '0006_alter_monthlylist_unit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monthlylist',
            name='unit',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
