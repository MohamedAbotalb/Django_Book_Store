# Generated by Django 5.0.3 on 2024-04-07 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_alter_category_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
