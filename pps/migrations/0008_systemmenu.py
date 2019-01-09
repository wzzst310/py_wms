# Generated by Django 2.1.5 on 2019-01-09 17:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pps', '0007_auto_20190110_0052'),
    ]

    operations = [
        migrations.CreateModel(
            name='SystemMenu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_column='name', max_length=255)),
                ('sn', models.CharField(db_column='sn', max_length=255)),
                ('url', models.CharField(db_column='url', max_length=255)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pps.SystemMenu')),
            ],
            options={
                'db_table': 'systemmenu',
            },
        ),
    ]
