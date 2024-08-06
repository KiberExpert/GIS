# Generated by Django 5.0.7 on 2024-08-06 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('username', models.CharField(max_length=60)),
                ('password', models.CharField(max_length=60)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('fullname', models.CharField(max_length=200)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
