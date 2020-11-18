# Generated by Django 3.0.7 on 2020-07-07 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration_ongc', '0007_auto_20200707_1306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='regform',
            name='CPF',
            field=models.CharField(default='NULL VALUE', max_length=60),
        ),
        migrations.AlterField(
            model_name='regform',
            name='Designation',
            field=models.CharField(default='NULL VALUE', max_length=60),
        ),
        migrations.AlterField(
            model_name='regform',
            name='Location',
            field=models.CharField(default='NULL VALUE', max_length=60),
        ),
        migrations.AlterField(
            model_name='regform',
            name='MobileNumber',
            field=models.CharField(default='NULL VALUE', max_length=15),
        ),
        migrations.AlterField(
            model_name='regform',
            name='PhoneNumber',
            field=models.CharField(default='NULL VALUE', max_length=15),
        ),
        migrations.AlterField(
            model_name='regform',
            name='Section',
            field=models.CharField(default='NULL VALUE', max_length=60),
        ),
    ]
