# Generated by Django 4.2.5 on 2023-10-05 08:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stockmgt', '0002_alter_stock_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='stock',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stockmgt.category'),
        ),
    ]
