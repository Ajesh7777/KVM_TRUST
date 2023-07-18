# Generated by Django 4.0.1 on 2022-05-18 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0027_notifications'),
    ]

    operations = [
        migrations.CreateModel(
            name='institution_list',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institution_name', models.CharField(max_length=150)),
                ('institution_picture', models.ImageField(blank=True, default='-', null=True, upload_to='img', verbose_name='file')),
                ('institution_link', models.CharField(max_length=150)),
            ],
        ),
    ]
