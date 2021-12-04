# Generated by Django 3.2.5 on 2021-12-04 11:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('body', models.TextField()),
                ('slug', models.SlugField(unique_for_date=True)),
                ('isComplted', models.BooleanField(default=False)),
                ('published', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]