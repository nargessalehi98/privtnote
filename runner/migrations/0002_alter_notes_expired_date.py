# Generated by Django 4.0.5 on 2022-06-24 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('runner', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='expired_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]