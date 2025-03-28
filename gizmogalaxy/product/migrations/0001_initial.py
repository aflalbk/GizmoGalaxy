# Generated by Django 5.1.7 on 2025-03-16 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('price', models.FloatField()),
                ('rating', models.FloatField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/product_image/')),
                ('stock', models.IntegerField(blank=True, null=True)),
                ('warranty', models.IntegerField(blank=True, null=True)),
                ('priority', models.IntegerField(default=0)),
                ('delete_status', models.IntegerField(choices=[(1, 'live'), (0, 'delete')], default=1)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
