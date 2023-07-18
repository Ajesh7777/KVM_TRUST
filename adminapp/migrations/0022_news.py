# Generated by Django 4.0.1 on 2022-05-17 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0021_delete_news'),
    ]

    operations = [
        migrations.CreateModel(
            name='news',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(blank=True, default='-', null=True, upload_to='img', verbose_name='file')),
                ('title', models.CharField(max_length=200)),
                ('post_date', models.CharField(max_length=60)),
                ('description', models.TextField()),
            ],
        ),
    ]