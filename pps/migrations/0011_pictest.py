# Generated by Django 2.1.5 on 2019-01-22 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pps', '0010_auto_20190110_2318'),
    ]

    operations = [
        migrations.CreateModel(
            name='PicTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gpic', models.ImageField(upload_to='pps')),
            ],
        ),
    ]
