# Generated by Django 3.2.16 on 2022-10-05 10:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20221005_1021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='subject',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.tagsubject'),
        ),
    ]