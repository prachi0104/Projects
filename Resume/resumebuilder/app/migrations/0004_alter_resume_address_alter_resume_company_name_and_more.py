# Generated by Django 4.0 on 2024-04-05 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_resume_year_of_passing'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='address',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='resume',
            name='company_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='resume',
            name='degree',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='resume',
            name='desc',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='resume',
            name='details',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='resume',
            name='dob',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='resume',
            name='email',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='resume',
            name='grade',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='resume',
            name='job_title',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='resume',
            name='maritial_status',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='resume',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='resume',
            name='nationality',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='resume',
            name='p_desc',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='resume',
            name='phn_no',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='resume',
            name='project_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='resume',
            name='project_title',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='resume',
            name='school',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='resume',
            name='skill_name',
            field=models.TextField(null=True),
        ),
    ]
