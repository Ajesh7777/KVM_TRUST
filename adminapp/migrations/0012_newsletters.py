# Generated by Django 4.0.1 on 2022-05-06 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0011_rename_career_careers'),
    ]

    operations = [
        migrations.CreateModel(
            name='newsletters',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pdf', models.FileField(upload_to='')),
            ],
        ),
    ]
