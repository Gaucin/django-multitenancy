# Generated by Django 2.1.7 on 2019-03-28 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('virket', '0002_task'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stuff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16)),
            ],
        ),
    ]
