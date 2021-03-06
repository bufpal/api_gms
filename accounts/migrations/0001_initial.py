# Generated by Django 2.1 on 2018-08-09 07:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fbuid', models.CharField(max_length=300)),
                ('ospid', models.CharField(max_length=300)),
                ('school', models.CharField(choices=[('a', '삼육대학교'), ('b', '한국전기직업전문학교'), ('c', '한국국제대학교')], max_length=1)),
                ('phone_number', models.CharField(max_length=20)),
                ('latlng', models.CharField(max_length=100)),
                ('level', models.CharField(blank=True, choices=[('Lv1', 'Lv1'), ('Lv2', 'Lv2'), ('Lv3', 'Lv3')], max_length=3)),
                ('avatar', models.CharField(blank=True, max_length=600)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('udpated_at', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
