# Generated by Django 3.0.5 on 2022-08-17 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0002_feedback'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_no', models.CharField(max_length=20, null=True)),
                ('image', models.FileField(null=True, upload_to='')),
                ('type', models.CharField(max_length=30, null=True)),
                ('price', models.CharField(max_length=30, null=True)),
                ('status', models.CharField(max_length=30, null=True)),
            ],
        ),
    ]
