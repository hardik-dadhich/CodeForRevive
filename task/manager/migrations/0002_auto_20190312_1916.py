# Generated by Django 2.0 on 2019-03-12 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup',
            name='mobile_no',
            field=models.IntegerField(),
        ),
    ]