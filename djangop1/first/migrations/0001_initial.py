# Generated by Django 3.0.5 on 2020-04-07 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='pics')),
                ('password', models.CharField(max_length=200)),
            ],
        ),
    ]
