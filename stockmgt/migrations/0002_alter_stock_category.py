# Generated by Django 4.2.5 on 2023-10-05 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stockmgt', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='category',
            field=models.CharField(blank=True, choices=[('Furniture', 'Furniture'), ('IT Equipment', 'IT Equipment'), ('Phone', 'Phone')], max_length=50, null=True),
        ),
    ]
