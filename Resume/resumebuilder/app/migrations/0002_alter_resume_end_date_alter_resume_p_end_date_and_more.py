# Generated by Django 4.0 on 2024-04-04 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='end_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='resume',
            name='p_end_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='resume',
            name='p_start_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='resume',
            name='start_date',
            field=models.DateField(null=True),
        ),
    ]