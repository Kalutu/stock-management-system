# Generated by Django 4.2.5 on 2023-10-09 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stockmgt', '0006_stockhistory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockhistory',
            name='timestamp',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
