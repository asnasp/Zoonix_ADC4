# Generated by Django 3.0.2 on 2020-01-29 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parlor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
