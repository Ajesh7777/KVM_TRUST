# Generated by Django 4.0.1 on 2022-05-06 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0012_newsletters'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsletters',
            name='month_year',
            field=models.CharField(default=1, max_length=150),
            preserve_default=False,
        ),
    ]
