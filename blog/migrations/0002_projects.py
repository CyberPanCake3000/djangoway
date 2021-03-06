# Generated by Django 3.2.12 on 2022-03-28 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('client', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('stack', models.CharField(max_length=100)),
                ('date_start', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
