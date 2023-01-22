# Generated by Django 4.2.dev20220621081037 on 2023-01-22 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SafeSight', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyOtherModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('age', models.IntegerField()),
                ('address', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]
