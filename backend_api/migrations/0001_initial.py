# Generated by Django 4.2.2 on 2023-06-13 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('genre', models.CharField(max_length=200)),
                ('starring', models.CharField(max_length=350)),
            ],
        ),
    ]
