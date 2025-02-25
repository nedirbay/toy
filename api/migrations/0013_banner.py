# Generated by Django 5.1.6 on 2025-02-25 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_alter_order_order_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='banners/')),
            ],
            options={
                'verbose_name': 'banner',
                'verbose_name_plural': 'bannerler',
                'db_table': 'banners',
            },
        ),
    ]
